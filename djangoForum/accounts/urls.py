from django.urls import path
from django.views.generic import TemplateView

from djangoForum.accounts.views import AccountLogin, AccountRegister, AccountLogout, AccountDetails, AccountDelete

urlpatterns = (
    path('login/', AccountLogin.as_view(), name='account login'),
    path('register/', AccountRegister.as_view(), name='account register'),
    path('<pk>', AccountDetails.as_view(), name='account details'),
    path('<pk>/delete/', AccountDelete.as_view(), name='account delete'),
    path('logout/', AccountLogout.as_view(), name='account logout'),
)