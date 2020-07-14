from django.db import models
from django.conf import settings

class Team(models.Model):
    """
    This table will belongs to department of various loactions
    """
    team_lead = models.CharField(max_length=150, blank=False,)
    department = models.DateField(null=False)
    average_pay = models.CharField(max_length=80, blank=False,)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
