from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee ,Department
from .serializers import DepartmentSerializer , EmployeeSerializer


class DepartmentView(APIView):
    def get(self , request):
        dept =Department.objects.all()
        serializer=DepartmentSerializer(dept,many=True)
        return Response(serializer.data)
    
class EmployeeView(APIView):
    def get(self,request,E_id=None , dept=None):
        if E_id is not None:
            try:
                employee = Employee.objects.all(E_id = E_id)
                emp_serializer = EmployeeSerializer(employee)
                return Response(emp_serializer.data)
            except Employee.DoesNotExist:
                return Response ({'message':'Employee Not Found'},status=status.HTTP_404_NOT_FOUND)
            
        elif dept is not None:
            try:
                dept = Employee.objects.filter(dept=dept)
                serializer = EmployeeSerializer(dept , many=True)
                return Response(serializer.data)
            except Department.DoesNotExist:
                return Response({'message':'No employee working'})
            
        employees = Employee.objects.all().order_by('-salary')
        employees_serializer = EmployeeSerializer(employees , many=True)
        return Response(employees_serializer.data,stauts=status.HTTP_200_OK)
   
       