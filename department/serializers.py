from rest_framework import serializers
from .models import Department
from teams.serializers import TeamSerializer

#--> Department Serializer
class DepartmentSerializer(serializers.ModelSerializer):
    team = TeamSerializer(source='teams', many=True,)
    class Meta:
        model = Department
        fields = ('pk', 'name', 'location', 'date_of_innaugration', 'team')
        read_only_fields = ('pk', 'created_at', 'updated_at')