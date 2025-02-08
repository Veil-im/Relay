from django.urls import path
from .views import CreateChatView

urlpatterns = [
    path("create/", CreateChatView.as_view(), name="create_chat"),
]

