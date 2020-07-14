from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Objective, Keyresult
from .serializers import ObjectiveCreateSerializer, KeyresultCreateSerializer, ObjectiveSerializer

class ObjectiveCreateAPIView(APIView):

    def post(self, request):
        response = {}
        serializer = ObjectiveCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["info"] = "objective added successfully"
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ObjectiveDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Objective.objects.get(pk=pk)
        except Objective.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objective = self.get_object(pk)
        serializer = ObjectiveSerializer(objective)
        return Response(serializer.data)

class KeyCreateAPIView(APIView):

    def post(self, request):
        response = {}
        serializer = KeyresultCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["info"] = "keyresult added successfully"
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KeyDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Keyresult.objects.get(pk=pk)
        except Keyresult.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        keyresult = self.get_object(pk)
        serializer = KeyresultCreateSerializer(objective)
        return Response(serializer.data)