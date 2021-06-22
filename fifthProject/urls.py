from django.contrib import admin
from django.urls import path,include
import blogApp.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogApp.views.home,name="home"),
    path('blog/<int:blog_id>',blogApp.views.detail,name="detail"),
    path('accounts/',include('accounts.urls')),
]
