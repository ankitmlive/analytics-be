from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import DepartmentSerializer
from .models import Department

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Department instances.
    """
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
