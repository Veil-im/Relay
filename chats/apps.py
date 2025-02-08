from django.apps import AppConfig


class ChatsConfig(AppConfig):
    default_auto_field = "models.primarys.SnowflakePrimaryKey"
    name = "chats"
