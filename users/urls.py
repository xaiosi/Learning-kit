"""为应用程序 users 定义 URL 模式"""
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')
]