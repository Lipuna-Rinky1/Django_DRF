from ast import Return
from django.shortcuts import render, redirect
from contactLibrary.models import ContactListLibrary
from .import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# create your views here

def register(request):
    if request.method == "POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'contactLibrary/register.html', {'form':form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('contact-list')
    else:
        form = AuthenticationForm()
    return render(request, 'contactLibrary/login.html', {'form':form})



def contact_list(request):
    contact_list = ContactListLibrary.objects.all()
    contacts = {'contact_list':contact_list}
    return render(request, 'contactLibrary/contacts.html', context=contacts)


def contact_create(request):
    form = forms.ContactListLibraryForm
    if request.method == "POST":
        form = forms.ContactListLibraryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/app/contact-list')
    else:
        form = forms.ContactListLibraryForm()
    return render(request, 'contactLibrary/contact_form.html', {'form':form} )











# ##############
# from django.contrib.auth import login

# from rest_framework import permissions
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.views import LoginView as KnoxLoginView

# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)

