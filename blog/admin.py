from django.contrib import admin
from .models import Category, Tag, Blog, Blog_description, Comment, Subscription

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Blog_description)
admin.site.register(Comment)
admin.site.register(Subscription)
