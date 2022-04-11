from django import forms

from djangoForum.forum.models import ForumPost, ForumThread, Profile, ForumCategory


class ForumCategoryForm(forms.ModelForm):
    class Meta:
        model = ForumCategory
        fields = ('title', 'description',)


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
