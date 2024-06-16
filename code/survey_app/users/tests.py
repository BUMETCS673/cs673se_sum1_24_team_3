from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from surveys.models import Survey, Question, Response

class SurveyTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(email='testuser@example.com', password='12345')
        self.survey = Survey.objects.create(title='Test Survey', description='Test Survey Description')
        self.question1 = Question.objects.create(survey=self.survey, text='Question 1')
        self.question2 = Question.objects.create(survey=self.survey, text='Question 2')
        
    def test_survey_list_view(self):
        self.client.login(email='testuser@example.com', password='12345')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Available Surveys')
        
    def test_take_survey_view(self):
        self.client.login(email='testuser@example.com', password='12345')
        response = self.client.get(reverse('take_survey', args=[self.survey.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.survey.title)

    def test_submit_survey(self):
        self.client.login(email='testuser@example.com', password='12345')
        response = self.client.post(reverse('take_survey', args=[self.survey.id]), {
            'form-0-answer': 1,
            'form-1-answer': 2,
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '0',
            'form-MIN_NUM_FORMS': '0',
            'form-MAX_NUM_FORMS': '1000',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Response.objects.count(), 2)
        
    def test_view_taken_survey(self):
        self.client.login(email='testuser@example.com', password='12345')
        response1 = self.client.post(reverse('take_survey', args=[self.survey.id]), {
            'form-0-answer': 1,
            'form-1-answer': 2,
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '0',
            'form-MIN_NUM_FORMS': '0',
            'form-MAX_NUM_FORMS': '1000',
        })
        response2 = self.client.get(reverse('view_survey', args=[self.survey.id]))
        self.assertEqual(response2.status_code, 200)
        self.assertContains(response2, 'Question 1')
        self.assertContains(response2, 'Question 2')
        self.assertContains(response2, 'Answer: I')
        self.assertContains(response2, 'Answer: II')
