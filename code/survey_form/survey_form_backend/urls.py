from django.urls import path, include
from rest_framework.routers import DefaultRouter
from survey_app.views import SurveyViewSet, QuestionViewSet, ResponseViewSet

router = DefaultRouter()
router.register(r"surveys", SurveyViewSet)
router.register(r"questions", QuestionViewSet)
router.register(r"responses", ResponseViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
