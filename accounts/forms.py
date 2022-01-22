from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Company

class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    country = forms.CharField(max_length=30, label='Country')
    COUNTRY_CHOICES =(
    ("1", "United States Of America"),
    ("2", "United Kingdom"),
    ("3", "Canada"),
)
    country = forms.ChoiceField(choices = COUNTRY_CHOICES)
 
    def save(self, request):
        user = super(CustomUserCreationForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.country = self.cleaned_data['country']
        user.save()
        return user

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'country', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')

class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'eni', 'address', 'zip']