

from re import template
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from pages.forms import AuctionForm

from pages.models import Auction


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self,*args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args,**kwargs)
        context['users'] = CustomUser.objects.all()
        return context



class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
# @login_required
class DashboardPageView(TemplateView):
    template_name = 'pages/dashboard.html'


from django.views.generic import ListView
from pages.models import Auction

class AuctionListView(View):

    form_class = AuctionForm

    def get(self, request, *args, **kwargs):
        object_list = Auction.objects.all()
        return render(request, "pages/auction_list.html", {'object_list': object_list})

   