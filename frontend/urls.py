from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from .views import index, comments_page
from rest_framework.authtoken import views as rest_auth_views

app_name = 'frontend'

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:id>/comments/', comments_page, name='comments')
]

