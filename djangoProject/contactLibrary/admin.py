from django.contrib import admin
from contactLibrary.models import ContactListLibrary

# Register your models here.
class ContactListLibraryAdmin(admin.ModelAdmin):
    list_display = ['id', "contact_id", "name","size","type","last_updated_on","creator","folder","used_in"]


admin.site.register(ContactListLibrary, ContactListLibraryAdmin)
