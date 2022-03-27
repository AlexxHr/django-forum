from django import forms

from djangoForum.forum.models import ForumPost


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ('content',)

