from rest_framework import serializers
from .models import Objective, Keyresult
from employees.models import Employee
from employees.serializers import EmployeeSerializer

class ObjectiveCreateSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), write_only=True)
    class Meta:
        model = Objective
        fields = ('id', 'text', 'employee')

class KeyresultCreateSerializer(serializers.ModelSerializer):
    objective = serializers.PrimaryKeyRelatedField(queryset=Objective.objects.all(), write_only=True)
    class Meta:
        model = Keyresult
        fields = ('id', 'status', 'due_date', 'objective')

class ObjectiveSerializer(serializers.ModelSerializer):
    result = KeyresultCreateSerializer(source='keyresults', many=True,)

    class Meta:
        model = Objective
        fields = ('id', 'text', 'result')