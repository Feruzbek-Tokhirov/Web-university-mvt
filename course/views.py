from django.shortcuts import render
from blog.models import Category

# Create your views here.


def course_view(request):
    category = Category.objects.all()
    context = {
        "categorys": category
    }
    return render(request, "courses.html", context)


def course_detail(request):
    return render(request, "course-single.html")
