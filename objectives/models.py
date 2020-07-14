from django.db import models
from django.conf import settings

from employees.models import Employee

class Objective(models.Model):
    """
    This table will belongs to department of various loactions
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="objectives")
    text = models.CharField(max_length=150, blank=False,)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
    
    def __str__(self):
        return '%d: %s' % (self.order, self.text)

class Keyresult(models.Model):
    """
    This table will hold key result status of objectives
    """
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE, related_name="keyresults")
    status = models.CharField(max_length=150, blank=False,)
    due_date = models.DateField(null=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

