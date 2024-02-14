from rest_framework import serializers
from .models import Todo

# Serializer using ModelSerializer, which automatically generates create and update methods
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description']

# Custom Serializer where create and update methods are explicitly defined
class TodoSerializer1(serializers.Serializer):
    # Define fields
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)

    # Create method - creates a new Todo object
    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
    
    # Update method - updates an existing Todo object
    # Here instance represents the existing data and validated_data represents the new data
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        print(instance.title)
        instance.description = validated_data.get('description', instance.description)
        print(instance.description)
        instance.save()
        return instance
    
    # Field-level validation for the title field
    def validate_title(self, value):
        if len(value) > 50:  # Check if the length of the title exceeds the limit
            raise serializers.ValidationError('Title is too long')  # Raise ValidationError if it exceeds the limit
        return value
