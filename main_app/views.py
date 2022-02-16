from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from platformdirs import user_cache_dir
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from .models import Planet, Profile
from django.views import View 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

@method_decorator(login_required, name='dispatch')

class ProfileView(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "profile.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home.html")
        else:
            context = {"form": form}
            return render(request, "profile.html", context)

class Landing(TemplateView):
    template_name = "landing.html"

class About(TemplateView):
    template_name = "about.html"

class Index(TemplateView):
    template_name = "index.html"




class Home(TemplateView):
    template_name = "home.html"
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
    fields = ['name', 'img', 'bio', 'verified_planet']
    template_name = "create.html"
    success_url = "/home/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Create, self).form_valid(form)
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

class Detail(DetailView):
    model = Planet
    template_name = "detail.html"

class Update(UpdateView):
    model = Planet
    fields = ['name', 'img', 'bio',]
    template_name = "update.html"
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})
   
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

# class CommentCreate(CreateView):
#     model = Comment
#     fields = ['name', 'title', 'comment']
#     template_name = "comment_create.html"
#     success_url = "/spacefarers/"

# class CommentUpdate(UpdateView):
#     model = Comment
#     fields = ['name', 'title', 'comment',]
#     template_name = "comment_update.html"
#     success_url = "/spacefarers/"

# class CommentDelete(DeleteView):
#     model = Comment
#     template_name = "comment_delete_confirmation.html"
#     success_url = "/spacefarers/"