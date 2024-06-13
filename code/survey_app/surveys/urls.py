from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ResponseViewSet, SurveyViewSet, QuestionViewSet


router = DefaultRouter()
router.register(r"surveys", SurveyViewSet)
router.register(r"questions", QuestionViewSet)
router.register(r"responses", ResponseViewSet)

urlpatterns = router.urls