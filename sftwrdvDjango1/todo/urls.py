from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [

    path("", views.home, name = 'home'),
    path("mydata/", views.mydata, name = 'mydata'),
    path("mydata/add", views.add, name = 'add'),


]