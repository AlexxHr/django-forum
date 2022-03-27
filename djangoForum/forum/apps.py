from django.apps import AppConfig


class ForumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djangoForum.forum'

    def ready(self):
        import djangoForum.forum.signals