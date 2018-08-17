from rest_framework import serializers
from .models import Students, Subjects

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('id', 'name', 'subject', 'marks')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ('id', 'subject', 'faculty')
