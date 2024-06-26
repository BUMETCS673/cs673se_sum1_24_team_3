"""
In order to Consolidate Serializers
Let's keep all user-related serializers in
code/survey_form/surveys/serializers.py
and all model-related serializers in
code/survey_form/survey_app/serializers.py.
"""

from rest_framework import serializers
from .models import Survey, Question, Response

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class SurveyDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Survey
        depth = 1
        fields = (
            'title',
            'description',
            'questions'
        )

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = "__all__"
