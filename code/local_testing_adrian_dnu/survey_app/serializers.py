"""
In order to Consolidate Serializers
Let's keep all user-related serializers in
code/survey_form/surveys/serializers.py
and all model-related serializers in
code/survey_form/survey_app/serializers.py.
"""

from rest_framework import serializers
from .models import Survey, Question, Response
from ..surveys.serializers import User


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = "__all__"


class Login:
    pass


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
