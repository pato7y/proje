from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)



class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    start_date = models.DateField(auto_now_add=True)
    annual_leave = models.FloatField(default=15.0)  # 15 gün izin

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)

    def late_minutes(self):
        if self.check_in and self.check_in.hour > 8:
            return (self.check_in - self.check_in.replace(hour=8, minute=0)).total_seconds() / 60
        return 0
class LeaveRequest(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )

    def __str__(self):
        return f"{self.employee.name}: {self.status}"
