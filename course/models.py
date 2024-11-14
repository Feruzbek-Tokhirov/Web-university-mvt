from django.db import models


# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField(upload_to="course")
    body = models.TextField()
    price = models.CharField(max_length=202, null=True, blank=True)
    description = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    lesson_number = models.CharField(max_length=202)
    time = models.CharField(max_length=202)
    title = models.CharField(max_length=202)
    body = models.CharField(max_length=202)
    video = models.CharField(max_length=202)


class Teacher(models.Model):
    full_name = models.CharField(max_length=202)
    image = models.ImageField(upload_to="teacher")
    job = models.CharField(max_length=202)
    description = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
