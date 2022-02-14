from django.urls import path
from . import views

urlpatterns = [
     path('', views.Home.as_view(), name="spacefarer"),
     path('about/', views.About.as_view(), name="about"),
     path('index/', views.Index.as_view(), name="index"),
     path('list/', views.WayfarerList.as_view(), name="spacefarer_list"),
     path('spacefarer/new/', views.WayfarerCreate.as_view(), name="spacefarer_create"),
     path('spacefarer/<int:pk>/', views.WayfarerDetail.as_view(), name="spacefarer_detail"),
     path('spacefarer/<int:pk>/update',views.WayfarerUpdate.as_view(), name="spacefarer_update"),
     path('spacefarer/<int:pk>/delete',views.WayfarerDelete.as_view(), name="spacefarer_delete"),


     path('accounts/signup/', views.Signup.as_view(), name="signup")
]