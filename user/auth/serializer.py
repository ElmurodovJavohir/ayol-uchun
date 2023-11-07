from rest_framework import serializers
# from ..models import User
from ..models import User


class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['first_name','last_name','phone_number','password1','password2']
    
    
    def create(self, validated_data):
        user = User.objects.create_user(
                validated_data['username'],
                password = validated_data['password'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
                )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'