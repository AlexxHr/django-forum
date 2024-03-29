from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from djangoForum.accounts.forms import AccountRegisterForm

User = get_user_model()


class AccountLogin(LoginView):
    template_name = 'accounts/account-login.html'


class AccountRegister(CreateView):
    template_name = 'accounts/account-register.html'
    form_class = AccountRegisterForm

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get_success_url(self):
        return reverse_lazy('home')


class AccountLogout(LogoutView):
    pass


class AccountDelete(UserPassesTestMixin, DeleteView):
    template_name = 'accounts/account-delete.html'

    def test_func(self):
        user = self.request.user
        obj = self.get_object()
        return obj == user or user.is_superuser

    def get_object(self, **kwargs):
        return get_object_or_404(User, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse_lazy('home')
