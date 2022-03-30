from django.contrib import admin
from django.urls import path
from . import views

urlpatterns= [
    path('',views.home),
    path('addUser',views.CreateAppliedUser.as_view()),
    path('viewUser',views.AppliedUserView.as_view()),
    path('verifyuser',views.VerifyUser.as_view())
]