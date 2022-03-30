from django.shortcuts import render
from .models import Question
from .serializers import QuestionSerializer
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class CreateQuestionview(APIView):
  
  def post(self,request,format=None):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

class QuestionsView(generics.ListAPIView):
    queryset=Question.objects.all()
    serializer_class = QuestionSerializer