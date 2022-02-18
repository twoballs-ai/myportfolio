from django.urls import path, include
from .views import index, services
from .views import *
from . import views
from django.contrib import admin

app_name = "sixg"

urlpatterns = [
    path('', index, name='index'),
    path('our-work/', our_work, name='our-work'),
    path('our-work-single/', our_work_single, name='our-work-single'),
    path('about/', about_us, name='about-us'),
    path('services/', services, name='services'),
    path('services-single/', services_single, name='services-single'),
    path('blog/', blog, name='blog'),
    path('contact/', views.contact, name='contact'),

]