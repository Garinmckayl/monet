from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm, CompanyUpdateForm
# Create your views here.



@login_required
def company(request):
    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, instance=request.user)
        p_form = CompanyUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.company)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('company')

    else:
        u_form = CustomUserChangeForm(instance=request.user)
        p_form = CompanyUpdateForm(instance=request.user.company)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'account/company.html', context)