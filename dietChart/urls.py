from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import LogoutView 

urlpatterns = [
      path("dietChart",views.dietChart,name="dietChart"),
      path("diets",views.diets,name="diets"),
      path("diets1",views.diets1,name="diets1"),
      path("",views.home1,name="home1"),
      path("foodTrack",views.foodTrack,name="foodTrack")
    #   path("cal",views.cal,name="cal")
]