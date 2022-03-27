from django.urls import path
from djangoForum.forum.views import ForumHomeView, ForumCategoryView, ForumPostCreateView

urlpatterns = [
    path('', ForumHomeView.as_view(), name='home'),
    path('forum/<pk>/', ForumCategoryView.as_view(), name='category threads'),
    path('forum/<pk>/<slug>/', ForumPostCreateView.as_view(), name='thread posts'),

]