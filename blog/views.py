from django.shortcuts import render, redirect
from .models import Category, Tag, Blog
from .forms import CommentForm, SubscriptionForm
from django.core.paginator import Paginator
from about.models import About
from course.models import Teacher


# Create your views here.


def index(request):
    category = Category.objects.all()
    about = About.objects.all()
    tech = Teacher.objects.all()
    blog = Blog.objects.all()[::-1]
    sub = SubscriptionForm(request.POST or None)
    if sub.is_valid():
        sub.save()
        return redirect(".")
    context = {
        "categorys": category,
        "sub": sub,
        "about": about,
        "tech": tech,
        "blogs": blog
    }
    return render(request, "index.html", context)


def blog(request):
    category = Category.objects.all()
    tag = Tag.objects.all()
    b = Blog.objects.all()
    p = Paginator(b, 1)
    page = request.GET.get('page')
    blog = p.get_page(page)
    sub = SubscriptionForm(request.POST or None)
    if sub.is_valid():
        sub.save()
        return redirect(".")
    context = {
        "categorys": category,
        "tags": tag,
        "blogs": blog,
        "sub": sub
    }
    return render(request, "blog.html", context)


def blog_detail(request, pk):
    category = Category.objects.all()
    tag = Tag.objects.all()
    blog = Blog.objects.get(id=pk)
    comment = CommentForm(request.POST or None)
    if comment.is_valid():
        com = comment.save(commit=False)
        com.blog = blog
        com.save()
        return redirect(".")
    sub = SubscriptionForm(request.POST or None)
    if sub.is_valid():
        sub.save()
        return redirect(".")
    ctx = {
        "categorys": category,
        "tags": tag,
        "blog": blog,
        "form": comment,
        "sub": sub
    }
    return render(request, "blog-single.html", ctx)
