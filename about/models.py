from django.db import models


# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField(upload_to="about")
    description = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=202)
    answer = models.CharField(max_length=202)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choose(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField(upload_to="choose")
    description = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
