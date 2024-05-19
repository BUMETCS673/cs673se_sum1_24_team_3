from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    choice_type = models.CharField(max_length=50)  # For example 'text', 'single_choice', 'multiple_choice'
