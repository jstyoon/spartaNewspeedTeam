from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import UserModel


class signup_form(UserCreationForm):
    
    class Meta:
        model = UserModel
        fields = ["username", "password1", "password2"]
