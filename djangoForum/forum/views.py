from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from djangoForum.forum.forms import ForumPostForm, ForumThreadForm, ProfileEditForm
from djangoForum.forum.models import ForumCategory, ForumThread, ForumPost, Profile

User = get_user_model()


class ForumHomeView(ListView):
    template_name = 'forum/home.html'
    model = ForumCategory


class ForumCategoryView(ListView):
    template_name = 'forum/category-threads.html'
    paginate_by = 5

    def get_queryset(self):
        category = ForumCategory.objects.get(slug=self.kwargs['slug'])
        object_list = ForumThread.objects.filter(category_id=category.id)
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = ForumCategory.objects.get(slug=self.kwargs['slug'])
        return context


class ForumThreadCreate(LoginRequiredMixin, CreateView):
    form_class = ForumThreadForm
    login_url = reverse_lazy('account login')
    template_name = 'forum/thread-create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.category = ForumCategory.objects.get(slug=self.kwargs['slug'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('category threads', kwargs={'slug': self.kwargs['slug']})


class ForumThreadView(ListView):
    template_name = 'forum/thread-posts.html'
    paginate_by = 5
    context_object_name = 'posts'

    def get_queryset(self):
        thread = ForumThread.objects.get(slug=self.kwargs['slug'])
        object_list = ForumPost.objects.filter(thread_id=thread.id)
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thread = ForumThread.objects.get(slug=self.kwargs['slug'])
        category = ForumCategory.objects.get(slug=thread.category.slug)
        context['thread'] = thread
        context['category'] = category
        return context


class ForumThreadEdit(UpdateView):
    template_name = 'forum/thread-edit.html'
    form_class = ForumThreadForm

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = self.request.user
        thread = self.get_object()
        if not (thread.user == user or user.is_superuser):
            raise PermissionDenied
        return handler

    def get_object(self, **kwargs):
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(ForumThread, slug=slug_)

    def get_success_url(self):
        return reverse_lazy('thread posts', kwargs={'slug': self.kwargs['slug']})


class ForumThreadDelete(DeleteView):
    template_name = 'forum/thread-delete.html'

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = self.request.user
        thread = self.get_object()
        if not (thread.user == user or user.is_superuser):
            raise PermissionDenied
        return handler

    def get_object(self, **kwargs):
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(ForumThread, slug=slug_)

    def get_success_url(self):
        thread = ForumThread.objects.get(slug=self.kwargs['slug'])
        category = ForumCategory.objects.get(slug=thread.category.slug)
        return reverse_lazy('category threads', kwargs={'slug': category.slug})


class ForumPostCreate(LoginRequiredMixin, CreateView):
    form_class = ForumPostForm
    login_url = reverse_lazy('account login')
    template_name = 'forum/post-create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.thread = ForumThread.objects.get(slug=self.kwargs['slug'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('thread posts', kwargs={'slug': self.kwargs['slug']})


class ForumPostReply(LoginRequiredMixin, CreateView):
    form_class = ForumPostForm
    login_url = reverse_lazy('account login')
    template_name = 'forum/post-reply.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reply_post'] = ForumPost.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        reply_post = ForumPost.objects.get(pk=self.kwargs['pk'])
        post.is_reply = True
        post.parent = reply_post
        post.user = self.request.user
        post.thread = ForumThread.objects.get(slug=reply_post.thread.slug)
        return super().form_valid(form)

    def get_success_url(self):
        reply_post = ForumPost.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy('thread posts', kwargs={'slug': reply_post.thread.slug})


class ForumPostEdit(UpdateView):
    template_name = 'forum/post-edit.html'
    form_class = ForumPostForm

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = self.request.user
        post = self.get_object()
        if not (post.user == user or user.is_superuser):
            raise PermissionDenied
        return handler

    def form_valid(self, form):
        post = form.save(commit=False)
        if form.initial['content'] != post.content:
            post.edited = True
        return super().form_valid(form)

    def get_object(self, **kwargs):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(ForumPost, pk=pk_)

    def get_success_url(self):
        post = get_object_or_404(ForumPost, pk=self.kwargs.get('pk'))
        return reverse_lazy('thread posts', kwargs={'slug': post.thread.slug})


class ForumPostDelete(DeleteView):
    template_name = 'forum/post-delete.html'

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = self.request.user
        post = self.get_object()
        if not (post.user == user or user.is_superuser):
            raise PermissionDenied
        return handler

    def get_object(self, **kwargs):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(ForumPost, pk=pk_)

    def get_success_url(self):
        post = get_object_or_404(ForumPost, pk=self.kwargs.get('pk'))
        return reverse_lazy('thread posts', kwargs={'slug': post.thread.slug})


class ProfileDetails(DetailView):
    model = User
    template_name = 'forum/profile-details.html'


class ProfileEdit(UpdateView):
    template_name = 'forum/profile-edit.html'
    form_class = ProfileEditForm

    def get_object(self, **kwargs):
        return get_object_or_404(Profile, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.kwargs.get('pk')})


class ProfilePosts(ListView):
    template_name = 'forum/profile-posts.html'
    paginate_by = 5

    def get_queryset(self):
        object_list = ForumPost.objects.filter(user_id=self.kwargs['pk'])
        return object_list


class SearchResults(ListView):
    template_name = 'forum/search-results.html'
    model = ForumThread

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list
