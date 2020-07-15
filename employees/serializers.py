from rest_framework import serializers
from department.models import Department
from .models import Employee, Team, Member

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'firstname', 'lastname', 'objective_count')

class TeamSerializer(serializers.ModelSerializer):
    lead = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), write_only=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), write_only=True)
    class Meta:
        model = Team
        fields = ('id', 'name', 'employee_count', 'objective_count', 'lead', 'department', 'average_pay')

class MemberSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), write_only=True)
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), write_only=True)
    class Meta:
        model = Member
        fields = ('employee', 'team',)