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
    Planet("Venus", "https://nypost.com/wp-content/uploads/sites/2/2021/11/astrology-venus-1a.jpg?quality=80&strip=all", "Now we mocve on to the second planet of our solar system Venus. Named after the infamous Venus Williams because it is the hottest planet. Even though Mercury is closer to the sun Venus is hotter because of sulfric acids clouds that trap the heat."),
    Planet("Earth" "https://discovery.sndimg.com/content/dam/images/discovery/editorial/Curiosity/2020/3/Earth-perfec-life-Shutterstock.jpg.rend.hgtvcom.616.347.suffix/1583192498207.jpeg", "On the the next on Earth there isnt really much to explain here simply the best planet there is in everyone opinon, has a bunch of weird species running around all the time especially those humans they're super weird."),
    Planet("Mars" "https://starwalk.space/gallery/images/mars-the-ultimate-guide/1920x1080.jpg", "On the the next on Earth there isnt really much to explain here simply the best planet there is in everyone opinon, has a bunch of weird species running around all the time especially those humans they're super weird."),
    Planet("Jupiter" "https://ak.picdn.net/shutterstock/videos/5290616/thumb/1.jpg", "On the the next on Earth there isnt really much to explain here simply the best planet there is in everyone opinon, has a bunch of weird species running around all the time especially those humans they're super weird."),
    Planet("Saturn" "https://www.worldatlas.com/r/w1200/upload/f3/0b/52/shutterstock-598786217.jpg", "On the the next on Earth there isnt really much to explain here simply the best planet there is in everyone opinon, has a bunch of weird species running around all the time especially those humans they're super weird."),
    Planet("Uranus" "https://mediaproxy.salon.com/width/1200/https://media.salon.com/2021/05/planet-uranus-0519211.jpg", "On the the next on Earth there isnt really much to explain here simply the best planet there is in everyone opinon, has a bunch of weird species running around all the time especially those humans they're super weird."),
    Planet("Neptune" "https://nypost.com/wp-content/uploads/sites/2/2021/11/astrology-neptune-sign-1a.jpg?quality=80&strip=all", "On the the next on Earth there isnt really much to explain here simply the best planet there is in everyone opinon, has a bunch of weird species running around all the time especially those humans they're super weird."),
    
]