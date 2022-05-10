from msilib import CreateRecord
from django.db import models
import datetime

# Create your models here.
class ContactListLibrary(models.Model):
    contact_id = models.CharField(max_length=10, blank=False)
    name = models.CharField(max_length=50)
    size = models.IntegerField(default=0, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True)
    last_updated_on = models.DateTimeField(default=datetime.datetime.now())
    creator = models.CharField(max_length=50, blank=True)
    folder = models.CharField(max_length=50, blank=True)
    used_in = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name
