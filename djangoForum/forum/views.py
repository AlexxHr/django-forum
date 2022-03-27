from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView

from djangoForum.forum.forms import ForumPostForm
from djangoForum.forum.models import ForumCategory, ForumThread, ForumPost


class ForumHomeView(ListView):
    template_name = 'forum/home.html'
    model = ForumCategory


class ForumCategoryView(ListView):
    template_name = 'forum/category-threads.html'

    def get_queryset(self):
        object_list = ForumThread.objects.filter(category_id=self.kwargs['pk'])
        return object_list


class ForumPostCreateView(CreateView):
    form_class = ForumPostForm
    template_name = 'forum/thread-posts.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.thread = ForumThread.objects.get(slug=self.kwargs['slug'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thread = ForumThread.objects.get(slug=self.kwargs['slug'])
        posts = ForumPost.objects.filter(thread_id=thread.id)
        context['posts'] = posts
        return context

    def get_success_url(self):
        return self.request.path