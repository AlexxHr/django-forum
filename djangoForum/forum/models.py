from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ForumCategory(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    slug = models.SlugField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ForumThread(models.Model):
    category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=30, null=True, blank=True)
    title = models.CharField(max_length=30, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ForumPost(models.Model):
    thread = models.ForeignKey(ForumThread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
