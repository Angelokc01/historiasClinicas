from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('', include('Historias.urls')),
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),
]

