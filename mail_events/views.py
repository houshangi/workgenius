from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


from asgiref.sync import async_to_sync
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from channels.layers import get_channel_layer
from .models import *


class HandleMandrillEventView(APIView):
    authentication_classes = []

    def post(self, request):
        mandrill_data = MandrillEvents.parse_raw(request.body.decode("utf-8"))
        for event in mandrill_data.mandrill_events:
            message_id = event.msg.id
            channel_layer = get_channel_layer()

            async_to_sync(channel_layer.group_send)(
                'mandrill_events',
                {
                    'type': 'event',
                    'message_id': message_id,
                    'event_type': "open"
                }
            )

        return Response({"status": "OK"})


@csrf_exempt
def index_view(request):
    return render(request, 'notify.html')