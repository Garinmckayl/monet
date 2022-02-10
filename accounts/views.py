
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.edit import UpdateView, CreateView

from accounts.models import Company

from .forms import (CompanyUpdateForm, CustomUserChangeForm,
                    CustomUserCreationForm)

# Create your views here.



@login_required
def company(request):
    if request.method == 'POST':
        # u_form = CustomUserChangeForm(request.POST, instance=request.user)
        p_form = CompanyUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.company)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('company')


    # u_form = CustomUserChangeForm(instance=request.user)
    p_form = CompanyUpdateForm(instance=request.user.company)

    context = {
        'p_form': p_form
    }

    return render(request, 'account/company.html', context)

class MyCompanyDetailView(View):
 
    def get(self, request, *args, **kwargs):
    
        my_company=Company.objects.filter(user=request.user).first()
        if my_company:
            return render(request, 'accounts/my-company.html',{"my_company": my_company})
        
        else:
            return redirect('company-create')



class CompanyUpdateView(UpdateView):
    model = Company
    fields = ['name', 'eni', 'address','zip']
    template_name_suffix = '_update_form'
   

class CompanyCreateView(CreateView):
    model = Company
    fields = ['name', 'eni', 'address', 'zip', 'entity_type']

    def form_valid(self, form):
        
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def connect(request):
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
        pass
    #     u_form = CustomUserChangeForm(instance=request.user)
    #     p_form = CompanyUpdateForm(instance=request.user.company)

    # context = {
    #     'u_form': u_form,
    #     'p_form': p_form
    # }

    return render(request, 'account/connect.html')
