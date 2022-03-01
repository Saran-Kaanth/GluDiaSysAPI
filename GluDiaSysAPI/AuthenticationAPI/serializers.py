from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(min_length=8,max_length=68,write_only=True)

    class Meta:
        model=get_user_model()
        fields=['email','username','password','mobile']
    
    def validate(self, attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')

        print("validation")
        if not username.isalnum():
            print("error")
            print(serializers.ValidationError)
            return serializers.ValidationError("Username must contain alphabets and numbers")
        return attrs

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
