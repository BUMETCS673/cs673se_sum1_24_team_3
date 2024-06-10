from django.contrib import admin
from .models import Survey, Question, Response, Instructor, Student, Course, StudentCourse, ExamQuestion, InstructorWeightedQuestion, StudentExamQuestion

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(StudentCourse)
admin.site.register(ExamQuestion)
admin.site.register(InstructorWeightedQuestion)
admin.site.register(StudentExamQuestion)
