from django.contrib import admin
from .models import Survey, Question, Response

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Response)
