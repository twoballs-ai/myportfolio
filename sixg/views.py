from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject ='пробное сообщение'
            body = {
                'first_name': form.cleaned_data['first_name'],
                'email':form.cleaned_data['email_address'],
                'message':form.cleaned_data['message']
            }
            message = '\n'.join(body.values())
            try:
                send_mail(subject,message,
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("sixg:index")

    form = ContactForm
    return render(request, 'sixg/contact.html', {'form':form})