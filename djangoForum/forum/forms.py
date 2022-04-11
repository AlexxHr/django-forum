from django import forms

from djangoForum.forum.models import ForumPost, ForumThread, Profile, ForumCategory


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ('content',)


class ForumThreadForm(forms.ModelForm):
    class Meta:
        model = ForumThread
        fields = ('title', 'content',)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'image',)
