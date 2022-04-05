from django import forms

from djangoForum.forum.models import ForumPost, ForumThread, Profile


class ForumPostForm(forms.ModelForm):
    content = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "class": "form-control",
                "style": "resize:none; height:150px"
            }
        ),
        label="Comment",
    )

    class Meta:
        model = ForumPost
        exclude = ('thread', 'user', 'edited', 'parent')


class ForumThreadForm(forms.ModelForm):
    class Meta:
        model = ForumThread
        fields = ('title', 'content',)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'image',)