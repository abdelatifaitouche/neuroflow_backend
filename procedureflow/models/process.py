
"""
from django.db import models






class Process(models.Model):
    process_name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.process_name



"""