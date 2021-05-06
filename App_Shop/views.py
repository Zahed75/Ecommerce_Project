from django.shortcuts import render
#import views
from django.views.generic import ListView, DetailView
#Models
from App_Shop.models import Product
#mixins
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Home(ListView):
    model = Product
    template_name='App_Shop/home.html'

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'
