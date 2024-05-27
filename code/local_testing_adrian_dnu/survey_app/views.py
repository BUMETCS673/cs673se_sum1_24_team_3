from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Survey, Question, Response as SurveyResponse
from .serializers import (
    SurveySerializer,
    QuestionSerializer,
    ResponseSerializer,
    UserSerializer,
    LoginSerializer,
)
from ..surveys.serializers import User


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = SurveyResponse.objects.all()
    serializer_class = ResponseSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    @staticmethod
    def post(request, *args, **kwargs):
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            access = RefreshToken.access_token
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(access),
                }
            )
        else:
            return Response(
                {"error": "Invalid Credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
