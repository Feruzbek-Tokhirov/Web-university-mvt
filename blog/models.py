from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField(upload_to="blog/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    tag = models.ManyToManyField(Tag, )

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Blog_description(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="descriptions")
    description = models.TextField()

    def __str__(self):
        return self.description[:30]


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comment")
    full_name = models.CharField(max_length=202)
    email = models.EmailField()
    message = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Subscription(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
