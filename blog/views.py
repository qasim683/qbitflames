from django.shortcuts import render
from .forms import *



def blog(request):
    if request.method == "GET":
        forms = BlogForm(request.get)
        
    return render(request, 'blog.html')

def blogsingle(request):
    return render(request, 'blog-single.html')