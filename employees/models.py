from django.db import models
#from teams.models import Team

class Employee(models.Model):
    firstname = models.CharField(verbose_name='full name', max_length=50, blank=False)
    lastname = models.CharField(verbose_name='last name', max_length=50, blank=False)
    #team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="employees")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname


