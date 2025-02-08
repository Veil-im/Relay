
from django.urls import re_path, path
from . import consumers
from channels.routing import URLRouter

urlpatterns = [
    re_path(r'chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]

websocket_urlpatterns = URLRouter([
    path('sync', urlpatterns)
])
