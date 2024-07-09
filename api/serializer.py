from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name= serializers.CharField()
    email= serializers.EmailField(required = False)
    address = serializers.CharField()
    age = serializers.IntegerField(required=False)


    def validate(self, attrs):
        name = attrs.get('name')
        email = attrs.get('email')
        address = attrs.get('address')
        errors = {}
        if len(name) <= 4:
            raise serializers.ValidationError("Name should not be less than 4 characters")
        if not name:
            errors['name'] = ["Name must be more than 4 characters"]
        
        if not email:
            errors['email'] = ["Email field is required"]
        
        if not address:
            errors['address'] = ["Address field is crazy"]

        if errors:
            raise serializers.ValidationError(errors)
        return attrs
    
    def create(self, validated_data):
        student = Student.objects.create(
            name=validated_data.get("name"),
            email=validated_data.get("email"),
            address=validated_data.get("address")
        )
        return student
    
    def update(self, instance, validated_data):
        return instance
    
