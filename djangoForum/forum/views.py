from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from djangoForum.forum.forms import ForumPostForm, ForumThreadForm
from djangoForum.forum.models import ForumCategory, ForumThread, ForumPost


class ForumHomeView(ListView):
    template_name = 'forum/home.html'
    model = ForumCategory


class ForumCategoryView(ListView):
    template_name = 'forum/category-threads.html'

    def get_queryset(self):
        category = ForumCategory.objects.get(slug=self.kwargs['slug'])
        object_list = ForumThread.objects.filter(category_id=category.id)
        return object_list


class ForumThreadCreate(LoginRequiredMixin, CreateView):
    form_class = ForumThreadForm
    template_name = 'forum/thread-create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.category = ForumCategory.objects.get(slug=self.kwargs['slug'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('category threads', kwargs={'slug': self.kwargs['slug']})


class ForumThreadView(CreateView):
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


class ForumThreadEdit(UpdateView):
    pass


class ForumThreadDelete(DeleteView):
    pass
