from django.urls import path
from .views import AddMemberView
urlpatterns = [
    path("add/", AddMemberView.as_view(), name="add_member"),
]

