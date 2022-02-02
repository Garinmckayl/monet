from unicodedata import name

from accounts import views as account_views
from django.urls import path, reverse

from .views import (AboutPageView, AuctionCreateView, AuctionListView,
                    DashboardPageView, HomePageView, StripeConnectionView,
                    auction_create_success)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('dashboard/company/', account_views.company, name="company"),
    path('dashboard/connect/', account_views.connect, name="connect"),
    path('auctions/', AuctionListView.as_view(), name='auctions'),
    path('auctions/create/',AuctionCreateView.as_view(), name= 'auction-create'),
    path('auctions/create/success/', auction_create_success, name='auction_create_success'),
    path('stripe-connection/', StripeConnectionView.as_view(), name='stripe-connection'),
    
]
