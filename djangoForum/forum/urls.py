from django.urls import path
from djangoForum.forum.views import ForumHomeView, ForumCategoryView, ForumThreadView, ForumThreadCreate, \
    ForumThreadDelete, ForumThreadEdit, ForumPostEdit, ForumPostDelete

urlpatterns = [
    path('', ForumHomeView.as_view(), name='home'),
    path('forum/<slug>/', ForumCategoryView.as_view(), name='category threads'),
    path('forum/<slug>/create', ForumThreadCreate.as_view(), name='thread create'),

    path('thread/<slug>/', ForumThreadView.as_view(), name='thread posts'),
    path('thread/<slug>/delete', ForumThreadDelete.as_view(), name='thread delete'),
    path('thread/<slug>/edit', ForumThreadEdit.as_view(), name='thread edit'),

    path('post/<pk>/edit', ForumPostEdit.as_view(), name='post edit'),
    path('post/<pk>/delete', ForumPostDelete.as_view(), name='post delete'),
]