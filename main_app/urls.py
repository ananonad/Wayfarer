from django.urls import path
from . import views

urlpatterns = [
     path('', views.Home.as_view(), name="home"),
     path('about/', views.About.as_view(), name="about"),
     path('index/', views.Index.as_view(), name="index"),
     path('wayfarer/', views.WayfarerList.as_view(), name="wayfarer_list"),
     path('wayfarer/new/', views.WayfarerCreate.as_view(), name="wayfarer_create"),
     path('wayfarer/<int:pk>/', views.WayfarerDetail.as_view(), name="wayfarer_detail"),
     path('wayfarer/<int:pk>/update',views.WayfarerUpdate.as_view(), name="wayfarer_update"),
     path('wayfarer/<int:pk>/delete',views.WayfarerDelete.as_view(), name="wayfarer_delete"),
     path('accounts/signup/', views.Signup.as_view(), name="signup")
]