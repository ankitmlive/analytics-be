from rest_framework import serializers
from department.models import Department
from employees.models import Employee
from .models import Team, EmployeeInTeam

class TeamSerializer(serializers.ModelSerializer):
    lead = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), write_only=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), write_only=True)
    class Meta:
        model = Team
        fields = ('id', 'name', 'lead', 'department', 'average_pay')

class TeamEmployeeSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), write_only=True)
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), write_only=True)
    class Meta:
        model = EmployeeInTeam
        fields = ('employee', 'team',)