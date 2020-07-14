from django.db import models
from department.models import Department

class Employee(models.Model):
    firstname = models.CharField(verbose_name='full name', max_length=50, blank=False)
    lastname = models.CharField(verbose_name='last name', max_length=50, blank=False)
    #team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="employees")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname

class Team(models.Model):
    lead = models.OneToOneField(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="teams")
    average_pay = models.CharField(max_length=200, blank=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        return "%s's Team" % (self.lead)


