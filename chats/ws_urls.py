
from django.urls import path
from . import consumers
from channels.routing import URLRouter

# All chats must be going through this url
urlpatterns = [
    path('chat/', consumers.ChatConsumer.as_asgi()),
]


websocket_urlpatterns = URLRouter([
    path('sync/', urlpatterns)
])
