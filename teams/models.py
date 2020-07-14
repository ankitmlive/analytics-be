from django.db import models
from django.conf import settings
from department.models import Department
from employees.models import Employee

class Team(models.Model):
    lead = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="team_lead")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="teams")
    average_pay = models.CharField(max_length=200, blank=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        return "%s's Team" % (self.lead)
    
class EmployeeInTeam(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="team")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="employee")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

