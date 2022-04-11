from django.urls import path

from djangoForum.accounts.views import AccountLogin, AccountRegister, AccountLogout, AccountDelete

urlpatterns = (
    path('login/', AccountLogin.as_view(), name='account login'),
    path('register/', AccountRegister.as_view(), name='account register'),
    path('<pk>/delete/', AccountDelete.as_view(), name='account delete'),
    path('logout/', AccountLogout.as_view(), name='account logout'),
)
