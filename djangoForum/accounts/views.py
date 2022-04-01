from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from djangoForum.accounts.forms import AccountRegisterForm, AccountEditForm
from djangoForum.forum.models import Profile

User = get_user_model()


class AccountLogin(LoginView):
    template_name = 'accounts/account-login.html'


class AccountRegister(CreateView):
    template_name = 'accounts/account-register.html'
    form_class = AccountRegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class AccountLogout(LogoutView):
    pass


class AccountDelete(DeleteView):
    template_name = 'accounts/account-delete.html'

    def get_object(self, **kwargs):
        return get_object_or_404(User, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse_lazy('home')


class AccountDetails(DetailView):
    model = User
    template_name = 'accounts/account-details.html'


class AccountEdit(UpdateView):
    template_name = 'accounts/account-edit.html'
    form_class = AccountEditForm

    def get_object(self, **kwargs):
        return get_object_or_404(Profile, pk=self.kwargs.get('pk'))

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     post = get_object_or_404(ForumPost, pk=self.kwargs.get('pk'))
    #     thread = ForumThread.objects.get(slug=post.thread.slug)
    #     context['thread'] = thread
    #     return context

    def get_success_url(self):
        return reverse_lazy('account details', kwargs={'pk': self.kwargs.get('pk')})