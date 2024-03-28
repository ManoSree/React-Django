from django.urls import path
from .views import EmployeeView, DepartmentView

urlpatterns = [
    path('employees/', EmployeeView.as_view(), name='All Employees'),
    path('employees/<int:E_id>', EmployeeView.as_view(), name='Employee'),
    path('employees/dept=<int:dept>', EmployeeView.as_view(), name="Employee by view"),
    
    path('departments/', DepartmentView.as_view(), name='Department')
]
