"""
ASGI config for relay project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter
from chats.ws_urls import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "relay.settings")
django.setup()

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),  # Handles HTTP requests
        "websocket": AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        ),
    }
)
