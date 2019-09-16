from django.db import models

# Create your models here.
class Branch(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    
    def payroll(self):
        employees = Employee.objects.filter(branch=self)
        total_payout = 0.00
        for employee in employees:
            total_payout += employee.salary 
        return total_payout
    

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)
    salary = models.FloatField(default=0)
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE)