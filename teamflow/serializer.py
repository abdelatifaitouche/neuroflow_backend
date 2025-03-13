from rest_framework import serializers
from .models import Process,Task
from procedureflow.models import Procedure




class TaskSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Task
        fields = "__all__"





class ProcessSerializer(serializers.ModelSerializer):

    tasks = TaskSerializer(many=True, read_only=True)  # Show tasks inside a process
    procedure = serializers.PrimaryKeyRelatedField(queryset=Procedure.objects.all())  # Link to a procedure

    class Meta : 
        model = Process
        fields = '__all__'
    

    def create(self, validated_data):
        process = Process.objects.create(**validated_data)

        for step in process.procedure.steps.all():
            Task.objects.create(
                process = process,
                title = step.title,
                step_number = step.step_number , 
                status = 'Pending'
            )

        return process