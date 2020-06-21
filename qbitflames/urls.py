from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('index/', index),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog-single/', blogsingle, name='blog-single'),
    path('leadrship/', leadrship, name='leadrship')
]
