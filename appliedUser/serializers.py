from attr import field
from rest_framework import serializers
from .models import AppliedUser

class AppliedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliedUser
        fields = ('name','designation','org','email','qualification','expertise')
        