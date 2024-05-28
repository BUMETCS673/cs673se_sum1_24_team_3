from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add additional fields here
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
