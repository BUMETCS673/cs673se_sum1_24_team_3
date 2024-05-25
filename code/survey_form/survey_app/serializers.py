from rest_framework import serializers
from .models import Survey, Question, Response


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class SurveySerializer(serializers.ModelSerializer):
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
        fields = '__all__'
