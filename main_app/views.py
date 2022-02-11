from django.shortcuts import render
from .models import Place
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
   
class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class Index(TemplateView):
    template_name = "index.html"

