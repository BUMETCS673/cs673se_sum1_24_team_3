from django.db import models
from django.conf import settings

class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='type the survey description here')
    
    def __str__(self):
        return self.title
    
class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
        
class Response(models.Model):
    ANSWER_CHOICES = [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IIII')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    answer = models.IntegerField(choices=ANSWER_CHOICES, default=1)

    def __str__(self):
        return f"{self.user.email} - {self.survey.title}"