from .models import Procedure
from .serializers import ProcedureSerializer

#the goal is to handle the creation of the procedures from here and not from the views



class ProcedureFactory : 
    @staticmethod
    def create_procedure(data , owner):
        """"
        Create a procedure
        """
        serializer = ProcedureSerializer(data = data)

        if serializer.is_valid():
            serializer.validated_data['owner'] = owner
            return serializer.save()

        return serializer.errors
    

    @staticmethod
    def update_procedure(procedure , data):
        
        if procedure.status == "Executed":
            return 


        serializer = ProcedureSerializer(procedure , data = data , partial = True)



        if serializer.is_valid():
            return serializer.save()


        return serializer.errors