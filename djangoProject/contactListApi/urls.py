
from django.contrib import admin
from django.urls import path, include
from .views import ContactCRUDCBV, GroupCRUDCBV

urlpatterns = [
    path('contacts', ContactCRUDCBV.as_view()),
    path('groups', GroupCRUDCBV.as_view()),
    # path('contact/<int:pk>', ContactCRUDCBV.as_view())
    
]
