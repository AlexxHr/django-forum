from django.db.models.signals import pre_save
from django.dispatch import receiver

from djangoForum.forum.models import ForumThread, ForumCategory
from djangoForum.util import unique_slug_generator


@receiver(pre_save, sender=ForumCategory)
@receiver(pre_save, sender=ForumThread)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
