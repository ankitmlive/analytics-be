from rest_framework import serializers
from department.models import Department
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'firstname', 'lastname',)