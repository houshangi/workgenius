from django.test import TestCase, Client
from django.urls import reverse
from channels.testing import WebsocketCommunicator
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .consumers import MandrillEventsConsumer


class HandleMandrillEventViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post(self):
        mandrill_data = {"mandrill_events": [{"msg": {"id": "12345"}}]}
        response = self.client.post(reverse("mandrill_event"), mandrill_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"status": "OK"})
        channel_layer = get_channel_layer()
        message = async_to_sync(channel_layer.receive)("mandrill_events")
        self.assertEqual(message["type"], "event")
        self.assertEqual(message["message_id"], "12345")
        self.assertEqual(message["event_type"], "open")


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notify.html")


class WebSocketTestCase(TestCase):
    async def test_consumer(self):
        communicator = WebsocketCommunicator(MandrillEventsConsumer.as_asgi(), "/ws/")
        connected, _ = await communicator.connect()
        self.assertTrue(connected)
        message = {"type": "event", "message_id": "12345", "event_type": "open"}
        await communicator.send_json_to(message)
        response = await communicator.receive_json_from()
        self.assertEqual(response, message)
        await communicator.disconnect()
