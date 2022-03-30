from attr import field
from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields=('content','op1','op2','op3','op4','answer','tags','difficulty','isVerified','createdAt')