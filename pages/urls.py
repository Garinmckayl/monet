from django.urls import path
from accounts import views as account_views


from .views import HomePageView, AboutPageView, DashboardPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('dashboard/company/', account_views.company, name="company"),
    path('dashboard/connect/', account_views.connect, name="connect"),
    
]
