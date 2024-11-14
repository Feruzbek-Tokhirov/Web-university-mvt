from django.urls import path
from .views import index, blog, blog_detail

urlpatterns = [
    path("", index, name="home"),
    path("blog/", blog),
    path("blog_detail/<int:pk>/", blog_detail),
]
