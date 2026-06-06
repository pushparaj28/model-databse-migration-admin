from django.contrib import admin
from django.contrib import admin

admin.site.site_header = "Pushpendra Admin Panel"
admin.site.site_title = "Pushpendra LMS "

admin.site.index_title = """
Welcome Pushpendra 🚀🧑‍💻
Manage Courses, Students and Instructors
"""  
# Register your models here.

from django.contrib import admin
from .models import (
    Instructor,
    Course,
    Student,
    Enrollment
)

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrollment)