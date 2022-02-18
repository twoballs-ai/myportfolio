from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
# Create your views here.

def index(request):
    return render(request, 'sixg/main.html')

def our_work(request):
    return render(request, 'sixg/our-work.html')

def our_work_single(request):
    return render(request, 'sixg/app-single.html')

def about_us(request):
    return render(request, 'sixg/about-us.html')

def services(request):
    return render(request, 'sixg/services.html')

def services_single(request):
    return render(request, 'sixg/services-single.html')

def blog(request):
    return render(request, 'sixg/blog.html')

def contact(request):
    return render(request, 'sixg/contact.html')