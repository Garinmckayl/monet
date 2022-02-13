
from pyexpat import model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from accounts.models import Company, CustomUser

from .forms import (CompanyUpdateForm, CustomUserChangeForm)


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

    return render(request, 'accounts/connect.html')


class AccountDetailView(View):
    
    def get(self, request, *args, **kwargs):
        user=request.user
       
        return render(request, 'accounts/account_detail.html', {'custom_user':user})