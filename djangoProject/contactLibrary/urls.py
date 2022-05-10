
from django.contrib import admin
from django.urls import path, include
from contactLibrary import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('contact-list', views.contact_list, name='contact-list'),
    path('contact-create', views.contact_create, name='contact-create'),
    
    
    
]
