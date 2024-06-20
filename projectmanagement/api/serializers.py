# myapp/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'client', 'users', 'created_at', 'created_by']
        read_only_fields = ['id', 'created_at', 'created_by']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['client'] = instance.client.name
        ret['created_by'] = instance.created_by.username if instance.created_by else None
        return ret

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Client
        fields = ['id', 'name', 'created_at', 'created_by', 'projects']
        read_only_fields = ['id', 'created_at', 'created_by']
