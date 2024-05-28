from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# If you're using a custom user model, register it like this:
# from .models import CustomUser
# admin.site.register(CustomUser, UserAdmin)

# For the default Django User model:
admin.site.register(CustomUser, UserAdmin)

