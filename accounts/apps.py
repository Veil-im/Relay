from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "models.primarys.SnowflakePrimaryKey"
    name = "accounts"
