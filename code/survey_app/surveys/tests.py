from django.test import TestCase
from .models import Survey, Question

class SurveyModelTest(TestCase):

    def setUp(self):
        self.survey = Survey.objects.create(title='Sample Survey', description='Sample Description')

    def test_create_survey(self):
        self.assertEqual(self.survey.title, 'Sample Survey')
        self.assertEqual(self.survey.description, 'Sample Description')

    def test_create_question(self):
        question = Question.objects.create(survey=self.survey, text='Sample Question')
        self.assertEqual(question.survey, self.survey)
        self.assertEqual(question.text, 'Sample Question')

    def test_create_multiple_surveys_and_questions(self):
        for i in range(1, 101):
            survey = Survey.objects.create(title=f'Survey {i}', description=f'Description {i}')
            question_text = f'Question {i} I.yes II.no III.maybe IIII.not sure'
            question = Question.objects.create(survey=survey, text=question_text)
            self.assertEqual(survey.title, f'Survey {i}')
            self.assertEqual(survey.description, f'Description {i}')
            self.assertEqual(question.survey, survey)
            self.assertEqual(question.text, question_text)
