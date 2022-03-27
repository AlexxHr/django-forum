from django.apps import AppConfig
from django.core.signals import request_finished


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djangoForum.accounts'

    def ready(self):
        import djangoForum.accounts.signals
