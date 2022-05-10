from django.shortcuts import render
from django.views import View
import io
from rest_framework.parsers import JSONParser
from contactListApi.models import Contact, Group
from contactListApi.serializers import ContactSerializer, GroupSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import json


class ContactCRUDCBV(View):


    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id', None)
        if id is not None:
            try:
                contact = Contact.objects.get(id = id)
                serializer = ContactSerializer(contact)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            except:
                msg = {"msg":"Contact not found"}
                json_data = JSONRenderer().render(msg)
                return HttpResponse(json_data, content_type='application/json', status=401)

        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json', status=200)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"contact created successfully"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json', status=200)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json', status=401)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get("id")
        contact = Contact.objects.get(id=id)
        serializer = ContactSerializer(contact, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"contact updated successfully"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get("id")
        try:
            contact = Contact.objects.get(id=id)
            if contact:
                contact.delete()
                msg = {"msg":"contact deleted successfully"}
                json_data = JSONRenderer().render(msg)
                return HttpResponse(json_data, content_type='application/json')
        except:
            msg = {"msg":"contact not found"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')



class GroupCRUDCBV(View):


    def get(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id', None)
        if id is not None:
            try:
                group = Group.objects.get(id = id)
                serializer = GroupSerializer(group)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            except:
                msg = {"msg":"Group not found"}
                json_data = JSONRenderer().render(msg)
                return HttpResponse(json_data, content_type='application/json')
        group = Group.objects.all()
        serializer = GroupSerializer(group, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = GroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"group created successfully"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get("id")
        group = Group.objects.get(id=id)
        serializer = GroupSerializer(group, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"group updated successfully"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get("id")
        try:
            group = Group.objects.get(id=id)
            if group and group.name:
                msg = {"msg":"You can't delete a group having name."}
                json_data = JSONRenderer().render(msg)
                return HttpResponse(json_data, content_type='application/json')
            else:
                group.delete()
                msg = {"msg":"group deleted successfully"}
                json_data = JSONRenderer().render(msg)
                return HttpResponse(json_data, content_type='application/json')
        except: 
            msg = {"msg":"Group not found"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')

