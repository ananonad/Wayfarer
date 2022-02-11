from django.shortcuts import render
from .models import Place
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
   
class Home(TemplateView):
    template_name = "home.html"

#...
class About(TemplateView):
    template_name = "about.html"

#...
class Index(TemplateView):
    template_name = "index.html"

class Planet:
    def __init__(self, name, img, bio):
        self.name = name
        self.img = img
        self.bio = bio

planets = [
    Planet("Mercury", "https://i.natgeofe.com/n/606b9e5c-68cb-49f9-8891-7b8c28919a2e/00000165-672f-d998-adf7-67bf0fd10000_3x2.jpg", "Welcome to the first planet of our solar system. Its deemed the first planet because it is the closet planet to our sun. Which also makes it extremely hot with an average temperatures of 430 degrees celsius during the day and 170 degrees celsius at night. Fun fact this is also the fastest moving planet in our solar system, revolving around the sun in 88 days."),
    Planet("Venus", "https://nypost.com/wp-content/uploads/sites/2/2021/11/astrology-venus-1a.jpg?quality=80&strip=all", "Now we mocve on to the second planet of our solar system Venus. Named after the infamous Venus Williams because it is the hottest planet. Even though Mercury is closer to the sun Venus is hotter because of sulfric acids clouds that trap the heat.")
]