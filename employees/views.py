from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer, TeamSerializer
from .models import Employee, Team

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

class TeamAPIView(APIView):
    def get(self, request):
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return Response(serializer.data)

class TeamCreateAPIView(APIView):
    
    def post(self, request):
        response = {}
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["info"] = "team added successfully"
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetailAPIView(APIView):
    pass