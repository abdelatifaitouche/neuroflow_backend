from django.db import models
from procedureflow.models import Procedure
from user_management.models import CustomUser
# Create your models here.



class Process(models.Model):
    process_name = models.CharField(max_length=100)
    description = models.TextField()
    responsable = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    procedure = models.ForeignKey(Procedure , on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[('Launched', 'Launched'), ('Halted', 'Halted'), ('Ended', 'Ended'), ('Aborted', 'Aborted')],
        default='Launched'
    )    

    def __str__(self):
        return self.process_name





class Task(models.Model):
    """Tasks generated from Procedure Steps"""
    process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name="tasks" , null=True)
    title = models.CharField(max_length=255 , null=True)
    step_number = models.PositiveIntegerField(null=True)
    content = models.TextField(null=True)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="assigned_tasks")
    status = models.CharField(null=True,
        max_length=50,
        choices=[("Pending", "Pending"), ("In Progress", "In Progress"), ("Completed", "Completed")],
        default="Pending"
    )

    class Meta:
        ordering = ["step_number"]  # Ensure tasks follow step order

    def __str__(self):
        return f"{self.process.process_name} - Step {self.step_number}: {self.title}"
