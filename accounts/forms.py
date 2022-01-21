from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    sex = forms.CharField()
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'firstname', 'lastname', 'password2', 'sex')

class CustomUserChangeForm(UserChangeForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'firstname', 'first_name', 'lastname')