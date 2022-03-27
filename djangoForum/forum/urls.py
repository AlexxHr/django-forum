from django.urls import path
from djangoForum.forum.views import ForumHomeView, ForumCategoryView, ForumThreadView

urlpatterns = [
    path('', ForumHomeView.as_view(), name='home'),
    path('forum/<slug>/', ForumCategoryView.as_view(), name='category threads'),
    path('thread/<slug>/', ForumThreadView.as_view(), name='thread posts'),

]