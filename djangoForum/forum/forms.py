from django import forms

from djangoForum.forum.models import ForumPost, ForumThread


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ('content',)


class ForumThreadForm(forms.ModelForm):
    class Meta:
        model = ForumThread
        fields = ('title', 'content',)
