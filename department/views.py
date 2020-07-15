from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import DepartmentSerializer, DepartmentDetailSerializer
from .models import Department

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Department instances.
    """
    def get_serializer_class(self):
        if self.action == 'list':
            return DepartmentSerializer
        if self.action == 'retrieve':
            return DepartmentDetailSerializer
    queryset = Department.objects.all()
