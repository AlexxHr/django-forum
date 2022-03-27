from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
from djangoForum.accounts.managers import ForumUserManager


class ForumUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    objects = ForumUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(ForumUser, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

