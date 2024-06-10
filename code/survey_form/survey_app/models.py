from django.db import models

class Instructor(models.Model):
    instructor_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.instructor_name
    
class Student(models.Model):
    student_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.student_name
    
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    number_credit = models.IntegerField()

    def __str__(self):
        return self.course_name

class StudentCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.grade}"

class CourseSurvey(models.Model):
    student_course = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    survey_rating = models.FloatField()
    course_survey_title = models.CharField(max_length=255)
    course_survey_description = models.TextField(blank=True, null=True)
    course_survey_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_survey_title

class CourseSurveyQuestion(models.Model):
    course_survey = models.ForeignKey(CourseSurvey, on_delete=models.CASCADE)
    survey_question = models.CharField(max_length=255)
    survey_choice_type = models.CharField(max_length=50)  # For example 'text', 'single_choice', 'multiple_choice'

    def __str__(self):
        return self.survey_question
    
class CourseSurveyChoice(models.Model):
    course_survey_question = models.ForeignKey(CourseSurveyQuestion, related_name='choices', on_delete=models.CASCADE)
    choice = models.CharField(max_length=255)

    def __str__(self):
        return self.choice

class CourseSurveyResponse(models.Model):
    student_course = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    course_survey_question = models.ForeignKey(CourseSurveyQuestion, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(CourseSurveyChoice, on_delete=models.CASCADE, null=True, blank=True)
    response = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.selected_choice:
            return self.selected_choice.choice
        return self.response
