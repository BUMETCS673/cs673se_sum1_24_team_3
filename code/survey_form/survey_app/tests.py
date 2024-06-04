from django.test import TestCase
from .models import Survey, Question

class SurveyModelTest(TestCase):

    def setUp(self):
        self.survey = Survey.objects.create(title='Sample Survey', description='Sample Description')

    def test_create_survey(self):
        self.assertEqual(self.survey.title, 'Sample Survey')
        self.assertEqual(self.survey.description, 'Sample Description')

    def test_create_question(self):
        question = Question.objects.create(survey=self.survey, text='Sample Question', choice_type='text')
        self.assertEqual(question.survey, self.survey)
        self.assertEqual(question.text, 'Sample Question')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_1(self):
        survey = Survey.objects.create(title='Survey 1', description='Description 1')
        question = Question.objects.create(survey=survey, text='Question 1', choice_type='text')
        self.assertEqual(survey.title, 'Survey 1')
        self.assertEqual(survey.description, 'Description 1')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 1')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_2(self):
        survey = Survey.objects.create(title='Survey 2', description='Description 2')
        question = Question.objects.create(survey=survey, text='Question 2', choice_type='text')
        self.assertEqual(survey.title, 'Survey 2')
        self.assertEqual(survey.description, 'Description 2')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 2')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_3(self):
        survey = Survey.objects.create(title='Survey 3', description='Description 3')
        question = Question.objects.create(survey=survey, text='Question 3', choice_type='text')
        self.assertEqual(survey.title, 'Survey 3')
        self.assertEqual(survey.description, 'Description 3')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 3')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_4(self):
        survey = Survey.objects.create(title='Survey 4', description='Description 4')
        question = Question.objects.create(survey=survey, text='Question 4', choice_type='text')
        self.assertEqual(survey.title, 'Survey 4')
        self.assertEqual(survey.description, 'Description 4')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 4')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_5(self):
        survey = Survey.objects.create(title='Survey 5', description='Description 5')
        question = Question.objects.create(survey=survey, text='Question 5', choice_type='text')
        self.assertEqual(survey.title, 'Survey 5')
        self.assertEqual(survey.description, 'Description 5')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 5')
        self.assertEqual(question.choice_type, 'text')


    def test_create_question_100(self):
        survey = Survey.objects.create(title='Survey 100', description='Description 100')
        question = Question.objects.create(survey=survey, text='Question 100', choice_type='text')
        self.assertEqual(survey.title, 'Survey 100')
        self.assertEqual(survey.description, 'Description 100')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 100')
        self.assertEqual(question.choice_type, 'text')


    def test_create_question_6(self):
        survey = Survey.objects.create(title='Survey 6', description='Description 6')
        question = Question.objects.create(survey=survey, text='Question 6', choice_type='text')
        self.assertEqual(survey.title, 'Survey 6')
        self.assertEqual(survey.description, 'Description 6')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 6')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_7(self):
        survey = Survey.objects.create(title='Survey 7', description='Description 7')
        question = Question.objects.create(survey=survey, text='Question 7', choice_type='text')
        self.assertEqual(survey.title, 'Survey 7')
        self.assertEqual(survey.description, 'Description 7')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 7')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_8(self):
        survey = Survey.objects.create(title='Survey 8', description='Description 8')
        question = Question.objects.create(survey=survey, text='Question 8', choice_type='text')
        self.assertEqual(survey.title, 'Survey 8')
        self.assertEqual(survey.description, 'Description 8')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 8')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_9(self):
        survey = Survey.objects.create(title='Survey 9', description='Description 9')
        question = Question.objects.create(survey=survey, text='Question 9', choice_type='text')
        self.assertEqual(survey.title, 'Survey 9')
        self.assertEqual(survey.description, 'Description 9')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 9')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_10(self):
        survey = Survey.objects.create(title='Survey 10', description='Description 10')
        question = Question.objects.create(survey=survey, text='Question 10', choice_type='text')
        self.assertEqual(survey.title, 'Survey 10')
        self.assertEqual(survey.description, 'Description 10')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 10')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_11(self):
        survey = Survey.objects.create(title='Survey 11', description='Description 11')
        question = Question.objects.create(survey=survey, text='Question 11', choice_type='text')
        self.assertEqual(survey.title, 'Survey 11')
        self.assertEqual(survey.description, 'Description 11')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 11')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_12(self):
        survey = Survey.objects.create(title='Survey 12', description='Description 12')
        question = Question.objects.create(survey=survey, text='Question 12', choice_type='text')
        self.assertEqual(survey.title, 'Survey 12')
        self.assertEqual(survey.description, 'Description 12')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 12')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_13(self):
        survey = Survey.objects.create(title='Survey 13', description='Description 13')
        question = Question.objects.create(survey=survey, text='Question 13', choice_type='text')
        self.assertEqual(survey.title, 'Survey 13')
        self.assertEqual(survey.description, 'Description 13')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 13')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_14(self):
        survey = Survey.objects.create(title='Survey 14', description='Description 14')
        question = Question.objects.create(survey=survey, text='Question 14', choice_type='text')
        self.assertEqual(survey.title, 'Survey 14')
        self.assertEqual(survey.description, 'Description 14')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 14')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_15(self):
        survey = Survey.objects.create(title='Survey 15', description='Description 15')
        question = Question.objects.create(survey=survey, text='Question 15', choice_type='text')
        self.assertEqual(survey.title, 'Survey 15')
        self.assertEqual(survey.description, 'Description 15')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 15')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_16(self):
        survey = Survey.objects.create(title='Survey 16', description='Description 16')
        question = Question.objects.create(survey=survey, text='Question 16', choice_type='text')
        self.assertEqual(survey.title, 'Survey 16')
        self.assertEqual(survey.description, 'Description 16')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 16')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_17(self):
        survey = Survey.objects.create(title='Survey 17', description='Description 17')
        question = Question.objects.create(survey=survey, text='Question 17', choice_type='text')
        self.assertEqual(survey.title, 'Survey 17')
        self.assertEqual(survey.description, 'Description 17')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 17')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_18(self):
        survey = Survey.objects.create(title='Survey 18', description='Description 18')
        question = Question.objects.create(survey=survey, text='Question 18', choice_type='text')
        self.assertEqual(survey.title, 'Survey 18')
        self.assertEqual(survey.description, 'Description 18')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 18')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_19(self):
        survey = Survey.objects.create(title='Survey 19', description='Description 19')
        question = Question.objects.create(survey=survey, text='Question 19', choice_type='text')
        self.assertEqual(survey.title, 'Survey 19')
        self.assertEqual(survey.description, 'Description 19')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 19')
        self.assertEqual(question.choice_type, 'text')

    def test_create_question_20(self):
        survey = Survey.objects.create(title='Survey 20', description='Description 20')
        question = Question.objects.create(survey=survey, text='Question 20', choice_type='text')
        self.assertEqual(survey.title, 'Survey 20')
        self.assertEqual(survey.description, 'Description 20')
        self.assertEqual(question.survey, survey)
        self.assertEqual(question.text, 'Question 20')
        self.assertEqual(question.choice_type, 'text')