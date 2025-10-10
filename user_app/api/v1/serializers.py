from django.contrib.auth.models import User
from rest_framework import serializers

class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ('username','email','password','confirm_password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

def validate(self,attrs):
    if attrs['password'] != attrs['confirm_password']:
        raise serializers.ValidationError("Passwords don't match")
    return attrs