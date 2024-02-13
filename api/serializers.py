from rest_framework import serializers
from .models import Todo

class TodoDeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=['title', 'description']
        def create(self, validate_data):
           return Todo.objects.create(**validate_data)
        
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=['title', 'description']