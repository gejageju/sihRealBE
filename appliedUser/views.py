from django.shortcuts import render
from django.http import HttpResponse,request
from .models import AppliedUser
from django.http import HttpResponse
from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework import generics,status
from .models import AppliedUser
from .serializers import AppliedUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AppliedUserSerializer
from django.http import JsonResponse
from rest_framework import serializers

def home(request):
    return render(request,'home.html')

class CreateAppliedUser(APIView):
    def post(self,request,format=None):
        serializer = AppliedUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

class AppliedUserView(generics.ListAPIView):
    queryset=AppliedUser.objects.all()
    serializer_class = AppliedUserSerializer



 
