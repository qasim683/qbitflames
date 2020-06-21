from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
    
        
        

        contact = Contact(name=name,email=email,subject=subject,message=message)
        
        contact.save()
    return render(request, 'contact.html')
    # if request.method == "POST":
    #     form = ContactForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return render(request, 'contact.html')
    # else:
    #     form = ContactForm()
        
            
        


def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blogsingle(request):
    
    return render(request, 'blog-single.html')

def leadrship(request):
    return render(request, 'leadership.html')


# recive data from users through contact form

# def contact_data(request):
#     if request.method == 'POST':
#         #form = ContactForm(request.POST)
#         name = request.POST.get('name', '')
#         email = request.POST.get('email', '')
#         subject = request.POST.get('subject', '')
#         message = request.POST.get('message', '')
#         print(name, email, subject, message)
#         #contact = Contact(name=name,email=email,subject=subject,message=message)
#         #contact.save()
        
#     return render(request, 'contact.html')
        