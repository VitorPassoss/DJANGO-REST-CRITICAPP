import os

import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import OriginValidator
from django.core.asgi import get_asgi_application
import api.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

django.setup()



application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": OriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    api.routing.websocket_urlpatterns,
                )
            ),
            ["*"],
        ),
    }
)
