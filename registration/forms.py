from django import forms
# from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Parollar mos emas!")


# class RegisterForm(forms.Form):
#     username = forms.CharField()
#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)
#
#     def validate_password(self, attrs):
#         pas1 = attrs["password1"]
#         pas2 = attrs["passsword2"]
#         if pas1 != pas2:
#             messages.error("Password error")
