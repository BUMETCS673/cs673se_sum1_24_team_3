from django.contrib import admin
from .models import CourseSurvey, CourseSurveyQuestion, Instructor, Student, Course, StudentCourse, CourseSurveyChoice, CourseSurveyResponse

admin.site.register(CourseSurvey)
admin.site.register(CourseSurveyQuestion)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(StudentCourse)
admin.site.register(CourseSurveyChoice)
admin.site.register(CourseSurveyResponse)
