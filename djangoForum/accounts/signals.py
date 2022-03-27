from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from djangoForum.accounts.models import Profile

userModel = get_user_model()

@receiver(post_save, sender=userModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)