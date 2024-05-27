from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class Question(models.Model):
    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name="questions"
    )
    text = models.CharField(max_length=255)
    choice_type = models.CharField(
        max_length=50
    )  # What types of choice ex MCR, MCQ, Free response


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()  # Can store both text response or chosen option
