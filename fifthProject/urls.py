from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import blogApp.views
import accounts.views
import photo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogApp.views.home,name="home"),
    path('blog/<int:blog_id>',blogApp.views.detail,name="detail"),
    path('accounts/',include('accounts.urls')),
    path('photo/',photo.views.photo,name='photo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
