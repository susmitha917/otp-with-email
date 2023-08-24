from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email' , 'password', 'is_verified']

class VerifyaccountSerializer(serializers.Serializer):
    email=serializers.EmailField()
    otp=serializers.CharField()
    