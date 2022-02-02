
import stripe
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

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



    def get(self, request, *args, **kwargs):
        object_list = Auction.objects.all()
        return render(request, "pages/auction_list.html", {'object_list': object_list})

class AuctionCreateView(CreateView):

    model = Auction
    fields = ['title', 'description', 'starting_price', 'category', 'active']

    def get_success_url(self):
        return reverse('auction_create_success')

    # form_class = AuctionForm

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         form.save()
    #         return HttpResponseRedirect('/success/')

    
    # def get(self, request, *arg, **kwargs):
    #     form = self.form_class(request.POST)
    #     return render(request, self.template_name)

def auction_create_success(request):

    return render(request, "pages/auction_create_success.html")


class StripeConnectionView(View):


    stripe.api_key = "sk_test_MkXB2zK4pVQk9vMHSCR4hrh100c70XITTM"
    stripe.client_id = "ca_L3q4MuEPR0JHtn2AlFe5bbf8TqrZDAcq"

    def get(self, request, *args, **kwargs):

        url = stripe.OAuth.authorize_url(scope='read_write')

        print("this is the url ........................", url)

        # return render(request, "pages/stripe-connection.html")
        return redirect(url)
