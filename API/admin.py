from django.contrib import admin
from .models import Department, Employee

class DepartmentAdmin(admin.ModelAdmin):
    list_display =['dept',]
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['E_name','salary','native']
    list_filter = ['dept']
    
admin.site.register(Employee , EmployeeAdmin)
admin.site.register(Department , DepartmentAdmin)


# Register your models here.

