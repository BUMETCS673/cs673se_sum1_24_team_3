from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Question(models.Model):
    QUESTION_TYPES = [
        ('text', 'Text'),
        ('multiple_choice', 'Multiple Choice'),
    ]

    type = models.CharField(max_length=50, choices=QUESTION_TYPES)
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class MultipleChoiceOption(models.Model):
    questions = models.ForeignKey(Question, related_name='mc_option', on_delete=models.CASCADE)
    text = models.CharField(max_length=1)
    correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class Response(models.Model):
    question = models.ForeignKey(Question, related_name='responses', on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text