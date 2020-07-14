from rest_framework import serializers
from .models import Employee

#--> auth serializers
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'firstname', 'lastname',)