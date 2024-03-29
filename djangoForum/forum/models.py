from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = CloudinaryField('image', null=True, blank=True)
    bio = RichTextField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def get_user_posts(self):
        posts = ForumPost.objects.filter(user_id=self.pk)
        return posts

    def get_user_threads(self):
        threads = ForumThread.objects.filter(user_id=self.pk)
        return threads

    def __str__(self):
        return self.user


class ForumCategory(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    slug = models.SlugField(max_length=30, null=True, blank=True)
    description = RichTextField(max_length=100, null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def get_all_threads(self):
        threads = ForumThread.objects.filter(category_id=self.pk)
        return threads

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_posted']


class ForumThread(models.Model):
    category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=30, null=True, blank=True)
    title = models.CharField(max_length=50, null=False, blank=False)
    content = RichTextField(max_length=1000, null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def get_thread_posts(self):
        posts = ForumPost.objects.filter(thread_id=self.pk)
        return posts

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']


class ForumPost(models.Model):
    thread = models.ForeignKey(ForumThread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(max_length=1000, null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    date_edited = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='replies')
    is_reply = models.BooleanField(default=False)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['date_posted']

    @property
    def children(self):
        return ForumPost.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False