# code/local_testing_adrian_dnu/myapp/urls.py

from django.urls import path
from .views import register_view, login_view, home_view, dashboard, take_survey, view_survey

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),  # Home URL
    path('dashboard/', dashboard, name='dashboard'),
    path('survey/<int:survey_id>/', take_survey, name='take_survey'),
    path('view_survey/<int:survey_id>/', view_survey, name='view_survey'),
]
