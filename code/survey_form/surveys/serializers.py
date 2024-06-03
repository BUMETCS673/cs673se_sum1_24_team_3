"""
In order to Consolidate Serializers
Let's keep all user-related serializers in 
code/survey_form/surveys/serializers.py
and all model-related serializers in
code/survey_form/survey_app/serializers.py.
"""

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "phone_number", "date_of_birth")
        extra_kwargs = {
            "username": {"required": True},
            "password": {"write_only": True},
            "phone_number": {"required": False},
            "date_of_birth": {"required": False},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            phone_number=validated_data.get("phone_number", ""),
            date_of_birth=validated_data.get("date_of_birth", None),
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
