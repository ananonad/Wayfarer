from django.shortcuts import render
from .models import Place
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class Home(View):
    def get(self, request):
        return HttpResponse("Wayfarer Home")



class About(View):

    def get(self, request):
        return HttpResponse("Wayfarer About")

class Index(View):

    def get(self, request):
        return HttpResponse("Wayfarer Index")
        
class Home(TemplateView):
    template_name = "home.html"

#...
class About(TemplateView):
    template_name = "about.html"

#...
class Index(TemplateView):
    template_name = "index.html"