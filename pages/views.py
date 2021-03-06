
import re
import requests
from accounts.models import Company, CustomUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView


from pages.models import Auction, Bid, DataSource


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['users'] = CustomUser.objects.all()
        return context


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
# @login_required


class DashboardPageView(TemplateView):
    template_name = 'pages/dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardPageView, self).get_context_data(
            *args, **kwargs)

        return context


class AuctionListView(ListView):
    model = Auction

    def get_context_data(self, *args, **kwargs):
        context = super(AuctionListView, self).get_context_data(
            *args, **kwargs)
        # company=Company.objects.get(user=self.request.user)
        # context['company'] = company

        return context


class MyAuctionDetailView(View):

    def get(self, request, *args, **kwargs):

        my_auction = Auction.objects.filter(user=request.user).first()
        if my_auction:
            return render(request, 'pages/my-auction-detail.html', {"my_auction": my_auction})

        else:
            return redirect('auction-create')


class AuctionCreateView(CreateView):

    model = Auction
    fields = ['description', 'starting_price', 'category', 'active']

    def form_valid(self, form):
        company = Company.objects.filter(user=self.request.user).first()
        if company:
            form.instance.user = self.request.user
            form.instance.company = company
            return super().form_valid(form)
        else:
            return redirect('company-create')

class AuctionUpdateView(UpdateView):
    model = Auction
    fields = ['description', 'starting_price', 'category', 'active']
    template_name_suffix = '_update_form'


class AuctionDetailView(DetailView):
    context_object_name = 'auction'
    queryset = Auction.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(AuctionDetailView, self).get_context_data(
            *args, **kwargs)

        company = Company.objects.get(user=self.request.user)
        context['company'] = company

        return context


class StripeConnectionView(View):

    # stripe.api_key = "sk_test_MkXB2zK4pVQk9vMHSCR4hrh100c70XITTM"
    # stripe.client_id = "ca_L3q4MuEPR0JHtn2AlFe5bbf8TqrZDAcq"

    def get(self, request, *args, **kwargs):

        # get the company of the user
        company, created = Company.objects.get_or_create(user=request.user)

        # at this time, the Company should be created at Codat
        baseUrl = "https://api-uat.codat.io"
        authHeaderValue = "Basic bDRlbDRiWDhwdGdhbzVYR1c2d2dxV0s2NHpEa3NOYTlIQk9wOVFEZQ=="
        # Add your authorization header
        headers = {"Authorization": authHeaderValue}
        # TODO first create the company
        data = {"name": "Recipe test company"}

        response = requests.post(
            'https://api.codat.io/companies', json=data, headers=headers)
        data = response.json()
        data_source, created = DataSource.objects.get_or_create(
            company=company)
        data_source.codat_id = data['id']
        data_source.save()

        redirect_url = data['redirect']

        # url = stripe.OAuth.authorize_url(scope='read_write')
        # company=Company.objects.first()

        # data, created= DataSource.objects.update_or_create(company=company, url=url)

        # print("this is the url ........................", url)

        # return render(request, "pages/stripe-connection.html")
        return redirect(redirect_url)


class DatasourceView(View):

    def get(self, request, *args, **kwargs):

        # get the company of the user
        company, created = Company.objects.get_or_create(user=request.user)

        # at this time, the Company should be created at Codat
        baseUrl = "https://api-uat.codat.io"
        authHeaderValue = "Basic bDRlbDRiWDhwdGdhbzVYR1c2d2dxV0s2NHpEa3NOYTlIQk9wOVFEZQ=="
        # Add your authorization header
        headers = {"Authorization": authHeaderValue}

        data_source, created = DataSource.objects.get_or_create(
            company=company)

        codat_id = data_source.codat_id

        print('codat id ....................', codat_id)

        response = requests.get(
            'https://api.codat.io/companies/'+codat_id, headers=headers)
        data = response.json()

        print('data, ........', data)
        print('hey .................',
              data['dataConnections'][0]['status'] == 'Linked')
        if data['dataConnections'][0]['status'] == 'Linked':

            data_source.codac_id = data['id']
            data_source.platform = data['platform']
            data_source.redirect = data['redirect']
            data_source.last_sync = data['lastSync']
            data_source.status = data['dataConnections'][0]['status']

            data_source.save()
            return render(request, 'pages/data-source.html', {'data_source': data_source})

        else:
            return redirect('company-create')

        def get_context_data(self, *args, **kwargs):
            context = super(DatasourceView, self).get_context_data(
                *args, **kwargs)

        company = Company.objects.get(user=self.request.user)
        context['company'] = company

        return context


class BidCreateView(CreateView):

    model = Bid
    fields = ['user', 'auction', 'bid_price']

    def get_absolute_url(self):
        return reverse('bid-detail', kwargs={'pk': self.pk})

    def get_context_data(self, *args, **kwargs):
        context = super(BidCreateView, self).get_context_data(*args, **kwargs)

        company = Company.objects.get(user=self.request.user)
        context['company'] = company

        return context


class BidDetailView(DetailView):
    context_object_name = 'bid'
    queryset = Bid.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(BidDetailView, self).get_context_data(*args, **kwargs)

        company = Company.objects.get(user=self.request.user)
        context['company'] = company

        return context
