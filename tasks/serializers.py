from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def get_user(self, obj):
        return obj.user.username  # Return the username instead of the ID
