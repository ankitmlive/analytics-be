from rest_framework import serializers
from .models import Department
from employees.serializers import TeamSerializer

#--> Department Serializer
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('pk', 'name', 'location', 'date_of_innaugration', 'employee_count')
        read_only_fields = ('pk', 'employee_count')

class DepartmentDetailSerializer(serializers.ModelSerializer):
    team = TeamSerializer(source='teams', many=True, read_only=True)
    class Meta:
        model = Department
        fields = ('pk', 'name', 'location', 'date_of_innaugration', 'team')
        read_only_fields = ('pk', 'created_at', 'updated_at')