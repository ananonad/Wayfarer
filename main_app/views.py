from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from platformdirs import user_cache_dir
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from .models import Planet
from django.views import View 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

class Landing(TemplateView):
    template_name = "landing.html"

class About(TemplateView):
    template_name = "about.html"

class Index(TemplateView):
    template_name = "index.html"

@method_decorator(login_required, name='dispatch')

class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # if name != None:
        #     context["planets"] = Planet.objects.filter(name__icontains=name, user=self.request.user)
        #     context["header"] = f"Searching for {name}"
        # else:
        #     context["planets"] = Planet.objects.all(user=self.request.user)
        #     context["header"] = "Trending Planets"
        return context

class List(TemplateView):
    template_name = "list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["planets"] = Planet.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["planets"] = Planet.objects.all()
            context["header"] = "Trending Planets"
        return context

class Create(CreateView):
    model = Planet
    fields = ['name', 'img', 'bio']
    template_name = "create.html"
    success_url = "/home/"

class Detail(DetailView):
    model = Planet
    template_name = "detail.html"

class Update(UpdateView):
    model = Planet
    fields = ['name', 'img', 'bio',]
    template_name = "update.html"
    success_url = "/home/"
   
class Delete(DeleteView):
    model = Planet
    template_name = "delete.html"
    success_url = "/home/"

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home.html")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
