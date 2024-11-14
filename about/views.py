from django.shortcuts import render, redirect

from blog.forms import SubscriptionForm
from .models import About, Choose, FAQ

# Create your views here.


def about(request):
    about = About.objects.all()
    chooes = Choose.objects.all()[::-1]
    faq = FAQ.objects.all()[::-1]
    sub = SubscriptionForm(request.POST or None)
    if sub.is_valid():
        sub.save()
        return redirect(".")
    contex = {
        "about": about,
        "choose": chooes,
        "faq": faq,
        "sub": sub
    }
    return render(request, "about.html", contex)
