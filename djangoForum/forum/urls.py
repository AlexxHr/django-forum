from django.urls import path
from djangoForum.forum.views import ForumHomeView, ForumCategoryView, ForumThreadView, ForumThreadCreate, \
    ForumThreadDelete, ForumThreadEdit, ForumPostEdit, ForumPostDelete, ProfileDetails, ProfileEdit, ProfilePosts, \
    ForumPostCreate, ForumPostReply, SearchResults, ProfileThreads

urlpatterns = [
    path('', ForumHomeView.as_view(), name='home'),
    path('search', SearchResults.as_view(), name='search results'),
    path('forum/<slug>/', ForumCategoryView.as_view(), name='category threads'),
    path('forum/<slug>/create', ForumThreadCreate.as_view(), name='thread create'),

    path('thread/<slug>/', ForumThreadView.as_view(), name='thread posts'),
    path('thread/<slug>/delete', ForumThreadDelete.as_view(), name='thread delete'),
    path('thread/<slug>/edit', ForumThreadEdit.as_view(), name='thread edit'),
    path('thread/<slug>/post', ForumPostCreate.as_view(), name='post create'),

    path('post/<pk>/reply', ForumPostReply.as_view(), name='post reply'),
    path('post/<pk>/edit', ForumPostEdit.as_view(), name='post edit'),
    path('post/<pk>/delete', ForumPostDelete.as_view(), name='post delete'),

    path('profile/<pk>', ProfileDetails.as_view(), name='profile details'),
    path('profile/<pk>/edit', ProfileEdit.as_view(), name='profile edit'),
    path('profile/<pk>/posts', ProfilePosts.as_view(), name='profile posts'),
    path('profile/<pk>/threads', ProfileThreads.as_view(), name='profile threads'),
]