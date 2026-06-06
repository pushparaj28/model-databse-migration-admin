from django.db import models

# Create your models here.
from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            'student',
            'course'
        )