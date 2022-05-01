from django.contrib import admin
from contactListApi.models import Contact, Group

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', "contact_id", "name","address","phone"]

class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', "group_id", "name"]

admin.site.register(Contact, ContactAdmin)
admin.site.register(Group, GroupAdmin)