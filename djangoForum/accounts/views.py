from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from djangoForum.accounts.forms import AccountRegisterForm


class AccountLogin(LoginView):
    template_name = 'accounts/account-login.html'


class AccountRegister(CreateView):
    template_name = 'accounts/account-register.html'
    form_class = AccountRegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class AccountLogout(LogoutView):
    pass


class AccountDetails(DetailView):
    model = get_user_model()
    template_name = 'accounts/account-details.html'
