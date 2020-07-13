from rest_framework import serializers
from .models import Department

#--> Department Serializer
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('pk', 'name', 'location', 'date_of_innaugration', 'created_at', 'updated_at')
        read_only_fields = ('pk', 'created_at', 'updated_at')