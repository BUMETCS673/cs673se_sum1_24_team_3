from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),  # Include your app's URLs here
    path('', include('myapp.urls')),  # You can use this to set the default view
]
