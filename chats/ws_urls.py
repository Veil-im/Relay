
from django.urls import re_path
from . import consumers
from channels.routing import URLRouter

websocket_urlpatterns = URLRouter([
    re_path(r'chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
])