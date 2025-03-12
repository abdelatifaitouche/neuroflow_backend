from user_management.models import Departement , CustomUser
from rest_framework.serializers import ModelSerializer




class DepartementSerializer(ModelSerializer):
    class Meta : 
        model = Departement
        fields = ["id" , "departement_name"]



class CustomUserSerializer(ModelSerializer):
    class Meta : 
        model = CustomUser
        fields = ["id" , "username" ,'departement', "email" , 'role']