from django.db import models
from django.contrib.auth.models import AbstractUser
from models.primarys import CUIDPrimaryKey

class Member(models.Model):
    id = CUIDPrimaryKey()
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)

    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
