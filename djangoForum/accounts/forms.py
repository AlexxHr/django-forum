from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django import forms

from djangoForum.forum.models import Profile


class AccountRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username")


class AccountEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'image',)


