from django.db import models
from user_management.models import CustomUser , Departement
# Create your models here.
from user_management.models import CustomUser



class Procedure(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)  # Short summary
    content = models.TextField(null=True , blank=True)  # Stores Rich Text (HTML)
    department = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="procedures" , null=True , blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('Draft', 'Draft'), ('Pending Approval', 'Pending Approval'), ('Active', 'Active'), ('Archived', 'Archived')],
        default='Draft'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    version = models.IntegerField(default=1)


    def merge_content(self):

        steps = self.steps.order_by('step_number')
        return "\n\n".join([step.content for step in steps if step.content])


    def __str__(self):
        return self.title
    

class ProcedureStep(models.Model):
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, related_name="steps")
    step_number = models.PositiveIntegerField()  # Defines the order of steps
    title = models.CharField(max_length=255)
    content = models.TextField()  # Rich Text content for the step
    writer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="written_steps")
    validator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="validated_steps")
    is_validated = models.BooleanField(default=False)  # Step validation status

    class Meta:
        ordering = ['step_number']  # Ensure steps are always retrieved in order

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"