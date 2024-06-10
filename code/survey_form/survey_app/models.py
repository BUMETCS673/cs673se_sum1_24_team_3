from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    choice_type = models.CharField(max_length=50)  # For example 'text', 'single_choice', 'multiple_choice'

    def __str__(self):
        return self.text

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()  # Can store both text responses or chosen options

    def __str__(self):
        return self.text

class Instructor(models.Model):
    instructor_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.instructor_name
    
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.student_name
    
class Course(models.Model):
    course_name = models.CharField(max_length=200)
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

class ExamQuestion(models.Model):
    exam_question = models.CharField(max_length=500)

    def __str__(self):
        return self.exam_question

class InstructorWeightedQuestion(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    exam_question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    weight = models.FloatField()

    def __str__(self):
        return f"{self.instructor} - {self.exam_question} - {self.weight}"

class StudentExamQuestion(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    instructor_weighted_question = models.ForeignKey(InstructorWeightedQuestion, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
