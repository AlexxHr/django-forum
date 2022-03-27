from django.contrib import admin

# Register your models here.
from djangoForum.accounts.models import ForumUser

admin.site.register(ForumUser)