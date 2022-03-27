from django.urls import path
from django.views.generic import TemplateView

from djangoForum.accounts.views import AccountLogin, AccountRegister, AccountLogout, AccountDetails

urlpatterns = (
    path('<pk>', AccountDetails.as_view(), name='account details'),
    path('login/', AccountLogin.as_view(), name='account login'),
    path('register/', AccountRegister.as_view(), name='account register'),
    path('logout/', AccountLogout.as_view(), name='account logout'),

)