"""
ASGI config for todo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
asgi_app = get_asgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

from channels.auth import AuthMiddlewareStack
import chatting.routing

application = ProtocolTypeRouter(
    {
        "http":asgi_app,
        "websocket":AuthMiddlewareStack(
        URLRouter(
            chatting.routing.websocket_urlpatterns
        ))
    }
    )
