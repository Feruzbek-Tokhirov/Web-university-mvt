from django.shortcuts import render, redirect

from blog.forms import SubscriptionForm
from .forms import ContactForm

# Create your views here.


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(".")
    sub = SubscriptionForm(request.POST or None)
    if sub.is_valid():
        sub.save()
        return redirect(".")
    contex = {
        "form": form,
        "sub": sub
    }
    return render(request, "contact.html", contex)
