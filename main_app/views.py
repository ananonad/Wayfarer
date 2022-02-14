from django.shortcuts import render
from .models import Planet
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
   
class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class Index(TemplateView):
    template_name = "index.html"



class WayfarerList(TemplateView):
    template_name = "Wayfarer_list.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["Wayfarers"] = Wayfarer 
    #     return context