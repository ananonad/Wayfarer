from django.urls import path
from . import views


urlpatterns = [
     path('', views.Landing.as_view(), name="landing"),
     path('about/', views.About.as_view(), name="about"),
     path('home/', views.Home.as_view(), name="home"),
     path('list/', views.List.as_view(), name="list"),
     path('new/', views.Create.as_view(), name="create"),
     path('<int:pk>/', views.Detail.as_view(), name="detail"),
     path('<int:pk>/update/',views.Update.as_view(), name="update"),
     path('<int:pk>/delete/',views.Delete.as_view(), name="delete"),
     path('accounts/signup/', views.Signup.as_view(), name="signup"),

     # path('profile/', views.ProfileView.as_view(), name='userprofile'),

     path('profile/create',  views.ProfileCreate.as_view(), name="create_profile"),
     path('<int:pk>/profile/update/', views.ProfileUpdate.as_view(), name="update_profile"),
     path('<int:pk>/profile/detail/', views.ProfileDetail.as_view(), name="detail_profile"),
     path('<int:pk>/profile/delete/', views.ProfileDelete.as_view(), name="profile_delete"),
     path('', views.logout, name="logout"),
     path('<int:pk>/comments/new/', views.CommentCreate.as_view(), name="comment_create"),
     path('<int:pk>/',views.modal),
]

