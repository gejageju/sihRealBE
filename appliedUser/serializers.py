from attr import field
from rest_framework import serializers
from .models import AppliedUser,VerifiedUser

class AppliedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliedUser
        fields = ('id','name','designation','org','email','qualification','expertise')

class VerifiedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifiedUser
        fields = ('id','name','designation','org','email','qualification','expertise')
        