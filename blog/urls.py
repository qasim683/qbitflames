from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', blog, name='blog'),
    path('blog-single/', blogsingle, name='blog-single'),
    
]
