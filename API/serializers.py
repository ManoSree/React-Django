from rest_framework import serializers
from .models import Department , Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        field='__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        field = '__all__'