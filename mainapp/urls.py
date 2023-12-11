from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

# from .views import home,register,login
from . import views

app_name = 'mainapp'

urlpatterns=[

    path('',views.index,name="index"),  
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('home/',views.home,name="home"),
   
    
] 