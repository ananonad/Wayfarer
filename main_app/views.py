from django.shortcuts import render

from django.views import View 
from django.http import HttpResponse
# Create your views here.

class Home(View):
    def get(self, request):
        return HttpResponse("Wayfarer Home")

# Create your views here.

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
