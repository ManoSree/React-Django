# from django.db import models
# import string
# import random

# def generate_unique_code():
#     length=6
    
#     while True:
#         code = ''.join(random.choices(string.ascii_uppercase,k=length))
#         if Room.objects.filter(code=code).count()==0:
#             break
#     return code    

# # Create your models here.

# class Room(models.Model):
#     code = models.CharField(max_length=8 , default=" ", unique=True)
#     host = models.CharField(max_length=50,unique=True)
#     guest_can_pause = models.BooleanField(null=False,default=False)
#     votes_to_skip = models.IntegerField(null=False,default=1)
#     created_at = models.DateTimeField(auto_now_add = True)    

from django.db import models

class Department(models.Model):
    dept = models.CharField(max_length=30)
    
    def __str__(self):
        return self.dept
    
class Employee(models.Model):
    E_id = models.AutoField(primary_key=True)
    E_name = models.CharField(max_length=40)
    dept = models.ForeignKey(Department , on_delete = models.CASCADE , related_name='department')
    salary = models.DecimalField(max_digits=10 , decimal_places=2)
    native = models.CharField(max_length=30)
     