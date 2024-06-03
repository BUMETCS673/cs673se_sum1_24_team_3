from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SurveyViewSet,
    QuestionViewSet,
    ResponseViewSet,
    RegisterView,
    LoginView,
)

router = DefaultRouter()
router.register(r"surveys", SurveyViewSet)
router.register(r"questions", QuestionViewSet)
router.register(r"responses", ResponseViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
