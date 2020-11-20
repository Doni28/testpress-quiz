from django.urls import path, include
from django.shortcuts import render
from . import views
urlpatterns = [
    path('',views.home, name ="home"),
    path('signup', views.signuppage, name ="signuppage"),
    path('login/', views.loginpage, name="loginpage"),
    path('logout/', views.logout, name="logout"), 
    path('index/', views.index, name="index"), 
    path('admin/', views.admin, name="admin"),
    path('computer/', views.computer, name="computer"),
    path('mathematics/', views.mathematics, name="mathematics"),
    path('politics/', views.politics, name="politics"),
    path('science/', views.science, name="science"),
    path('gk/', views.gk, name="gk"),
    path('sports/', views.sports, name="sports"),

]
