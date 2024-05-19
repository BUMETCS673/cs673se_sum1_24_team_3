from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import SurveyViewSet, QuestionViewSet, ResponseViewSet

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'responses', ResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
