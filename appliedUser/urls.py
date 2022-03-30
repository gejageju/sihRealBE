from django.contrib import admin
from django.urls import path
from . import views

urlpatterns= [
    path('',views.home),
    path('add',views.CreateAppliedUser.as_view()),
    path('view',views.AppliedUserView.as_view()),
]