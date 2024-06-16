from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Survey, Question, Response
from django.contrib.auth import get_user_model

class SurveyAPITests(APITestCase):

    def setUp(self):
        self.survey = Survey.objects.create(title='API Survey', description='API Survey Description')
        self.question = Question.objects.create(survey=self.survey, text='API Question')
        self.staff_user = get_user_model().objects.create_user(email='staff@example.com', password='12345', is_staff=True)
        self.non_staff_user = get_user_model().objects.create_user(email='user@example.com', password='12345')

    def test_get_surveys(self):
        url = reverse('survey-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_survey_as_staff_user(self):
        self.client.login(email='staff@example.com', password='12345')
        url = reverse('survey-list')
        data = {'title': 'New Survey', 'description': 'New Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Survey.objects.count(), 2)
        self.assertEqual(Survey.objects.get(id=response.data['id']).title, 'New Survey')

    def test_create_survey_as_non_staff_user(self):
        self.client.login(email='user@example.com', password='12345')
        url = reverse('survey-list')
        data = {'title': 'New Survey', 'description': 'New Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Survey.objects.count(), 1)

    def test_get_questions(self):
        url = reverse('question-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_question_as_staff_user(self):
        self.client.login(email='staff@example.com', password='12345')
        url = reverse('question-list')
        data = {'survey': self.survey.id, 'text': 'New Question'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 2)
        self.assertEqual(Question.objects.get(id=response.data['id']).text, 'New Question')

    def test_create_question_as_non_staff_user(self):
        self.client.login(email='user@example.com', password='12345')
        url = reverse('question-list')
        data = {'survey': self.survey.id, 'text': 'New Question'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Question.objects.count(), 1)
