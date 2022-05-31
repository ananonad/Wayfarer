from multiprocessing import context
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from platformdirs import user_cache_dir
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from .models import Planet, Comment, Profile, User
from django.views import View 
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms



 
class Landing(TemplateView):
    template_name = "landing.html"

# @method_decorator(login_required, name='dispatch')
class About(TemplateView):
    template_name = "about.html"

class Index(TemplateView):
    template_name = "index.html"


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

@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["planets"] = Planet.objects.all()
        context["comments"] = Comment.objects.all()
        return context
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     name = self.request.GET.get("name")
    #     print('=================================================')
    #     print(User.objects.filter(username=self.request.user))
    #     # print(self.request.query_params.get('id'))
    #     print(name)
        
    #     print('=================================================')
    #     if name != None:
    #         context["planets"] = Planet.objects.filter(name__icontains=name)
    #         context["header"] = f"Searching for {name}"
    #         context['profile'] = Profile.objects.filter(name=self.request.user)
    #         context['user'] = User.objects.filter(username = self.request.user)
    #     else:
    #         context["planets"] = Planet.objects.all()
    #         context["header"] = "Trending Planets"
    #         context['profile'] = Profile.objects.filter(name=self.request.user)
    #         # context['user'] = User.objects.filter(id = self.kwargs['pk'])
    #     return context
        



class List(TemplateView):
    template_name = "list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["planets"] = Planet.objects.filter(user=self.request.user, name__icontains=name)
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


class ProfileCreate(CreateView):
    model = Profile
    fields = ['img', 'location', 'bio']
    template_name = 'create_profile.html'
    current_user = User.id
    success_url = f"/list/{current_user}"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreate).form_valid(form)

    def get_success_url(self):
        return reverse('detail_profile', kwargs={'pk': self.object.pk})
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['profile'] = Profile.objects.filter()
    #     return context

class ProfileDetail(DetailView):
    model = Profile
    template_name = "detail_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['user'] = User.objects.filter(id = self.kwargs['pk'])
        print(self.request.user)
        context['user'] = Profile.objects.filter(user=self.request.user)
        return context

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['img', 'location', 'bio', 'name']
    template_name = 'update_profile.html'

    def get_success_url(self):
        return reverse('detail_profile', kwargs={'pk': self.object.pk})

class ProfileDelete(DeleteView):
    model = Profile
    template_name = "profile_delete_confirmation.html"
    success_url = "/home/"


class Detail(DetailView):
    model = Planet
    template_name = "detail.html"
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.all()
        return context

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



def logoutuser(request):
    logout(request)
    return render ('landing.html')


class CommentCreate(CreateView):
    model = Comment
    fields = ['user','title', 'comment', 'planet']
    template_name = "comment_create.html"

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        title = request.POST.get("title")
        comment = request.POST.get("comment")
        planet = Planet.objects.get(pk=request.POST.get("planet"))
        Comment.objects.create(user=user, title=title, comment=comment, planet=planet)
        return redirect('home')

        
class CommentUpdate(UpdateView):
    model = Comment
    fields = ['name', 'title', 'comment',]
    template_name = "comment_update.html"
    success_url = "/list/"

# class CommentDelete(DeleteView):
#     model = Comment
#     template_name = "comment_delete_confirmation.html"
#     success_url = "/spacefarers/"
class CommentDelete(DeleteView):
    model = Comment
    template_name = "comment_delete_confirmation.html"
    success_url = "/list/"

def modal(request):
    model = Comment
    field = ['title', 'comment']
    title = request.POST.get("title")
    comment = request.POST.get("comment")
    return render(request,'commentcreate.html',{"form":UserCreationForm})
