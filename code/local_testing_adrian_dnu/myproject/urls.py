# code/local_testing_adrian_dnu/myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('', include('myapp.urls')),  # Include the home URL
]
