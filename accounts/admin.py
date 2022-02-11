from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Company

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name']

class CompanyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Company._meta.fields]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Company, CompanyAdmin)