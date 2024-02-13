from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=['title', 'description']

        def create(self, validate_data):
           return Todo.objects.create(**validate_data)
        
    # Here instance is the old data and validated data is new data

        def update(self, instance, validated_data):
            instance.title=validated_data.get('title', instance.title)
            print(instance.title)
            instance.description=validated_data.get('description', instance.description)
            print(instance.description)
            instance.save()
            return instance


