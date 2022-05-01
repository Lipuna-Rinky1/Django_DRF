from rest_framework import serializers
from contactListApi.models import Contact, Group

class ContactSerializer(serializers.Serializer):
    contact_id = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    address = serializers.CharField(max_length=40, required=False, allow_blank=True)
    phone = serializers.CharField(max_length=10, required=False, allow_blank=True)

    def  create(self, validated_data):
        return Contact.objects.create(**validated_data)

    def  update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance

class GroupSerializer(serializers.Serializer):
    group_id = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=30, required=False, allow_blank=True)

    def  create(self, validated_data):
        return Group.objects.create(**validated_data)

    def  update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance