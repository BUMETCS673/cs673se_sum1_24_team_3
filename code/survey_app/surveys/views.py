from rest_framework import viewsets, status, generics
from rest_framework.response import Response


from .models import Survey, Question, Response as SurveyResponse
from .serializers import (
    SurveySerializer,
    QuestionSerializer,
    ResponseSerializer
)

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = SurveyResponse.objects.all()
    serializer_class = ResponseSerializer
