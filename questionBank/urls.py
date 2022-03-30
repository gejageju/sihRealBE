from django import views
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('addQuestion',views.CreateQuestionview.as_view()),
    path('getQuestions',views.QuestionsView.as_view())
    
]