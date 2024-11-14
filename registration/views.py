from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
# from .models import UserProfile
# from django.contrib.auth.forms import UserCreationForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data["username"],
                                password=data["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home")
                else:
                    return HttpResponse("You did not log in")
            else:
                return HttpResponse("You have a mistake in the password")
    else:
        form = LoginForm()
        ctx = {
            "form": form
        }
        return render(request, "registration/login.html", ctx)


def user_logout(request):
    if not request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request, "registration/logged_out.html")


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password1=form.cleaned_data['password1'],
                password2=form.cleaned_data['password2']
            )
            # UserProfile.objects.create(user=user, phone=form.cleaned_data['phone'])
            login(request, user)
            return redirect('home')  # Home sahifasiga o'tish
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})



# def user_register(request):
#     if request.user.is_authenticated:
#         return redirect("home")
#     form = RegisterForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect("home")
#     context = {
#         "form": form
#     }
#     return render(request, "registration/register.html", context)


# def user_register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = RegisterForm()
#     return render(request, 'registration/register.html', {'form': form})
