from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from djangoForum.forum.models import ForumThread, ForumCategory
from djangoForum.util import unique_slug_generator


@receiver(pre_save, sender=ForumCategory)
@receiver(pre_save, sender=ForumThread)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# create permission for editing upon creation
# @receiver(post_save, sender=ForumThread)
# def post_save_receiver(sender, instance, *args, **kwargs):
#     u = get_user_model().objects.get(pk=instance.user_id)
#     permission = Permission.objects.get(codename='change_forumthread')
#     u.user_permissions.add(permission)
#     print(u.user_permissions)
