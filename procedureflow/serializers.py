from rest_framework.serializers import ModelSerializer
from .models import *
from user_management.serializers import CustomUserSerializer

class ProcedureStepSerializer(ModelSerializer):
    class Meta : 
        model = ProcedureStep
        fields = "__all__"


class ProcedureSerializer(ModelSerializer):

    #steps = ProcedureStepSerializer(many = True , read_only = True)

    owner = CustomUserSerializer(many = False , read_only = True)

    class Meta : 
        model = Procedure
        fields = "__all__"

