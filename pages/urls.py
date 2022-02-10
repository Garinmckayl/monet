from unicodedata import name

from accounts import views as account_views
from django.urls import path, reverse

from .views import (AboutPageView, AuctionCreateView, AuctionDetailView, AuctionListView, BidCreateView, BidDetailView,
                    DashboardPageView, DatasourceView, HomePageView, StripeConnectionView,MyAuctionDetailView,AuctionUpdateView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('auctions/', AuctionListView.as_view(), name='auctions'),
    path('auction-detail/<int:pk>/', AuctionDetailView.as_view(), name='auction-detail'),
    path('auctions/create/',AuctionCreateView.as_view(), name= 'auction-create'),
    path('bids/create/',BidCreateView.as_view(), name= 'bid-create'),
    path('bid-detail/<int:pk>/', BidDetailView.as_view(), name='bid-detail'),
    path('stripe-connection/', StripeConnectionView.as_view(), name='stripe-connection'),
    path('data-source/',DatasourceView.as_view(), name='data-source'),
    path('dashboard/my-auction/', MyAuctionDetailView.as_view(),name='my-auction'),
    path('auction-update/<int:pk>/',AuctionUpdateView.as_view(), name='auction-update'),
    
    path('dashboard/company/my-company', account_views.MyCompanyDetailView.as_view(), name='my-company'),
    path('dashboard/company/<int:pk>/', account_views.CompanyUpdateView.as_view(), name="company-update"),
    path('dashboard/company/create/', account_views.CompanyCreateView.as_view(), name='company-create'),
    path('dashboard/connect/', account_views.connect, name="connect"),
    
]
