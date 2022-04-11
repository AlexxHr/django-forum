from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('djangoForum.accounts.urls')),
    path('', include('djangoForum.forum.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'djangoForum.forum.views.handler404'
handler403 = 'djangoForum.forum.views.handler403'
