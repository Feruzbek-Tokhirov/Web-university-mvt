from django.urls import path
from .views import course_view, course_detail

urlpatterns = [
    path("", course_view, name="courses"),
    path("detail/", course_detail, name="courses_detail")
]
