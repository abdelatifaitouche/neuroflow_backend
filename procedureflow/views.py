from django.shortcuts import render , get_object_or_404
from .models import * 
from .serializers import * 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework import status

from .permissions import *


from user_management.authenticate import CustomAuthentication
from .factories import ProcedureFactory
# Create your views here.



class ProcedureListView(APIView):
    authentication_classes = [CustomAuthentication]


    def get(self ,request):

        filters = {}

        if status:=request.query_params.get("status"):
            filters['status'] = status

        if department:= request.query_params.get('department'):
            filters['department'] = department
        
        query_set = Procedure.objects.filter(**filters).order_by("-created_at")

        
        procedures_serializer = ProcedureSerializer(query_set , many = True)
        return Response({"response" : procedures_serializer.data})
    
    def post(self , request):

        procedure = ProcedureFactory.create_procedure(request.data , request.user) #factory handling the creaiton of procedure
        if procedure : 
            return Response({"response" : ProcedureSerializer(procedure).data} , status=status.HTTP_201_CREATED)
        
        return Response({'response' : "invalid data"} , status=status.HTTP_400_BAD_REQUEST)


class ProcedureDetailView(APIView):
    authentication_classes = [CustomAuthentication]
    def get(self , request , pk):
        procedure_model = get_object_or_404(Procedure , pk = pk)

        merged_content = procedure_model.merge_content()


        procedure_serializer = ProcedureSerializer(procedure_model)

        response_data = procedure_serializer.data
        response_data['merged_content'] = merged_content


        return Response({"response" : response_data} , status=status.HTTP_200_OK)
    
    def put(self , request , pk):

        procedure_model = get_object_or_404(Procedure , pk = pk)
        
        procedure = ProcedureFactory.update_procedure(procedure_model , request.data)

        if procedure : 
            return Response({"response": ProcedureSerializer(procedure).data}, status=status.HTTP_201_CREATED)

        return Response({"response" : "invalid data"} , status=status.HTTP_400_BAD_REQUEST)

       

        
    
    def patch(self , request , pk):
        procedure_model = get_object_or_404(Procedure , pk = pk)

        procedure = ProcedureFactory.update_procedure(procedure_model , request.data)

        if procedure : 
            return Response({"response": ProcedureSerializer(procedure).data}, status=status.HTTP_201_CREATED)

        return Response({"response" : "invalid data"} , status=status.HTTP_400_BAD_REQUEST)
   
   
    def delete(self, request, pk):
        procedure = get_object_or_404(Procedure, pk=pk)
        procedure.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


                



class ProcedureStepListView(APIView):

    authentication_classes = [CustomAuthentication]

    def get(self , request , pk):
        procedure_steps_model = ProcedureStep.objects.filter(procedure = pk)

        #self.check_object_permissions(request , procedure_steps_model)

        procedure_steps_serializer = ProcedureStepSerializer(procedure_steps_model , many = True)

        return Response({"response" : procedure_steps_serializer.data})
    


    def post(self , request , pk):
        procedure_step_serializer = ProcedureStepSerializer(data = request.data)

        if procedure_step_serializer.is_valid():
            procedure_step_serializer.save()
            return Response({"response" : procedure_step_serializer.data} , status=status.HTTP_201_CREATED)
        print(procedure_step_serializer.errors)
        return Response({"response" : procedure_step_serializer.errors} , status = status.HTTP_400_BAD_REQUEST)
    


class StepDetailView(APIView):
    authentication_classes = [CustomAuthentication]


    def get(self , request , step_id):
        
        step_model = ProcedureStep.objects.get(id = step_id)

        step_serializer = ProcedureStepSerializer(step_model , many = False)

        return Response({'response' : step_serializer.data} , status=status.HTTP_200_OK)
    


    def post(self , request , pk):
        return
    

    def delete(self , request , pk):
        return 
    


    def put(self , request , pk):
        return 
    

    def patch(self , request , pk):
        return





