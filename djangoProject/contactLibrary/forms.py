from pyexpat import model
from django import forms
from contactLibrary.models import ContactListLibrary


class ContactListLibraryForm(forms.ModelForm):
    class Meta:
        model = ContactListLibrary
        fields = "__all__"

