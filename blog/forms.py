from .models import Comment, Subscription
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ["blog"]


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"
