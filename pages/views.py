from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required



class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
# @login_required
class DashboardPageView(TemplateView):
    template_name = 'pages/dashboard.html'