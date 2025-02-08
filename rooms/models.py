from django.db import models
from models.primarys import CUIDPrimaryKey

class Room(models.Model):
    id = CUIDPrimaryKey()

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


