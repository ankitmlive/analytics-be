from django.db import models
from django.conf import settings

class Department(models.Model):
    """
    This table will belongs to department of various loactions
    Location can be a foreign key
    """
    name = models.CharField(max_length=80, blank=False,)
    location = models.CharField(max_length=150, blank=False,)
    date_of_innaugration = models.DateField(null=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
    
    @property
    def employee_count(self):
        return self.teams.all().count()
