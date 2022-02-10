from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView

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

class CompanyUpdateView(UpdateView):
    model = Company
    fields = ['name', 'user','eni']
    template_name_suffix = '_update_form'
    def get_context_data(self,*args, **kwargs):
        context = super(CompanyUpdateView, self).get_context_data(*args,**kwargs)
        p_form = CompanyUpdateForm(self.request.POST,
                                   self.request.FILES,
                                   instance=self.request.user.company)
        context['p_form']=p_form
        
        company=Company.objects.get(user=self.request.user)
        context['company'] = company
        
        return context



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
