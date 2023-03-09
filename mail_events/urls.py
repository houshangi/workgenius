from django.urls import path
from .views import index_view,HandleMandrillEventView

urlpatterns = [path("index/", index_view, name="handle_index"),
               path("send-event/", HandleMandrillEventView.as_view(), name="handle_event_view")]
