# code/local_testing_adrian_dnu/myapp/urls.py

from django.urls import path
from .views import register_view, login_view, home_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),  # Home URL
]
