from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import Employee

from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Employee instances.
    """
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
