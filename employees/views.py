from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import Employee

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Employee instances.
    """
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
