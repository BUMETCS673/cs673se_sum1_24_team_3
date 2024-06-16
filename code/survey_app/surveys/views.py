from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .permissions import IsStaffOrReadOnly

from .models import Survey, Question, Response as SurveyResponse
from .serializers import (
    SurveySerializer,
    QuestionSerializer,
    ResponseSerializer
)

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [IsStaffOrReadOnly]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsStaffOrReadOnly]

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = SurveyResponse.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [IsStaffOrReadOnly]
