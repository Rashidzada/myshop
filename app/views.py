from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .import models
# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        models.Contact.objects.create(name = name, email = email , subject = subject , message = message)
        messages.success(request,'Your message has been sent. Thank you!')
        return redirect('index')
    return render(request,'index.html')


def blog(request):
    return render(request,'blog.html')


def blog_details(request):
    return render(request,'blog_details.html')


def portfolio_details(requset):
    return render(requset,'portfolio_details.html')


def services_details(request):
    return render(request,'services_details.html')