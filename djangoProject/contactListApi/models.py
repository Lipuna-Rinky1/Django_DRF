from django.db import models
from rest_framework import serializers

# Create your models here.
class Contact(models.Model):
    contact_id = models.CharField(max_length=10, blank=False)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=10)

class Group(models.Model):
    group_id = models.CharField(max_length=10, blank=False)
    name = models.CharField(max_length=30, blank=True)
   