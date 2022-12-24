from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
 re_path(r'wss/chatting/conversation/(?P<idcnv>)\w+/$', consumers.Conversation.as_asgi()),   
]
