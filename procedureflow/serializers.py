from rest_framework.serializers import ModelSerializer
from .models import *

class ProcedureStepSerializer(ModelSerializer):
    class Meta : 
        model = ProcedureStep
        fields = "__all__"


class ProcedureSerializer(ModelSerializer):

    #steps = ProcedureStepSerializer(many = True , read_only = True)

    class Meta : 
        model = Procedure
        fields = "__all__"

