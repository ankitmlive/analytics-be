from django.db import models
from django.conf import settings
from department.models import Department

class Employee(models.Model):
    """
    A Basic EMployee Model holds all the user in app
    In Production it will be a DJANGO AUTH USER
    New Fields can be added later
    """
    firstname = models.CharField(verbose_name='full name', max_length=50, blank=False)
    lastname = models.CharField(verbose_name='last name', max_length=50, blank=False)

    def __str__(self):
        return self.firstname
    
    @property
    def objective_count(self):
        return self.objectives.all().count()

class Team(models.Model):
    """
    A Model that will hold All Teams in app
    New Fields can be added later
    """
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="teams")
    lead = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="manager")
    members = models.ManyToManyField(Employee, through='Member')
    average_pay = models.CharField(max_length=200, blank=False)

    @property
    def name(self):
        return "%s's Team" % (self.lead)
    
    @property
    def employee_count(self):
        return self.members.all().count()

    @property
    def objective_count(self):
        obj = 0
        for mem in self.members.all():
            obj += mem.objectives.all().count()
        return obj
    
class Member(models.Model):
    """
    A Model that will hold All dtails of employess in a Team
    Strict Contraint are not applied yet, It is (depending on requirements)
    New Fields can be added later
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="member")  
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="member_team")


