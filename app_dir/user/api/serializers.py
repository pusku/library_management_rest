from rest_framework import serializers
from django.contrib.auth import get_user_model
from app_dir.user.models import UserProfile

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['avatar',]

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'profile',
            'email',
            'password',
            'is_staff',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        is_staff = validated_data['is_staff']
        user_obj = User(
            username=username,
            email=email,
            is_staff=is_staff
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance
