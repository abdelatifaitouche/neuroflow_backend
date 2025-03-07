from django.shortcuts import render , get_object_or_404
from .models import * 
from .serializers import * 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework import status

from .permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication


from user_management.authenticate import CustomAuthentication
# Create your views here.


class ProcedureListView(APIView):
    authentication_classes = [CustomAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self ,request):

        filters = {}

        if status:=request.query_params.get("status"):
            filters['status'] = status

        if department:= request.query_params.get('department'):
            filters['department'] = department
        
        query_set = Procedure.objects.filter(**filters)

        
        procedures_serializer = ProcedureSerializer(query_set , many = True)
        return Response({"response" : procedures_serializer.data})
    
    def post(self , request):

        data = request.data
        procedure_serializer = ProcedureSerializer(data = data)
        if procedure_serializer.is_valid():
            procedure_serializer.validated_data['owner'] = request.user
            procedure_serializer.save()
            return Response({"response" : procedure_serializer.data} , status=status.HTTP_201_CREATED)
        return Response({"response" : procedure_serializer.errors} , status=status.HTTP_400_BAD_REQUEST)


class ProcedureDetailView(APIView):

    permission_classes = [AllowAny]        
    def get(self , request , pk):
        procedure_model = get_object_or_404(Procedure , pk = pk)

        merged_content = procedure_model.merge_content()


        procedure_serializer = ProcedureSerializer(procedure_model)

        response_data = procedure_serializer.data
        response_data['merged_content'] = merged_content


        return Response({"response" : response_data} , status=status.HTTP_200_OK)
    
    def put(self , request , pk):

        procedure_model = get_object_or_404(Procedure , pk = pk)

        procedure_serializer = ProcedureSerializer(instance = procedure_model , data = request.data)

        if procedure_serializer.is_valid():
            procedure_serializer.save()
            return Response({"response" : procedure_serializer.data} , status=status.HTTP_201_CREATED)
        
        return Response({"response" : procedure_serializer.errors} , status=status.HTTP_400_BAD_REQUEST)


        
    
    def patch(self , request , pk):
        procedure_model = get_object_or_404(Procedure , pk = pk)

        procedure_serializer = ProcedureSerializer(instance = procedure_model , data = request.data , partial = True)

        if procedure_serializer.is_valid():
            procedure_serializer.save()
            return Response({"response" : procedure_serializer.data} , status=status.HTTP_201_CREATED)
        
        return Response({"response" : procedure_serializer.errors} , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , pk):
        procedure_model = get_object_or_404(Procedure , pk = pk)
        procedure_model.delete()
        return Response({"response" : "Procedure Deleted"} , status=status.HTTP_200_OK)
    


                



class ProcedureStepListView(APIView):
    permission_classes = [UpdatePermissions , IsAuthenticated]
    def get(self , request , pk):
        procedure_steps_model = ProcedureStep.objects.filter(procedure = pk)

        self.check_object_permissions(request , procedure_steps_model)

        procedure_steps_serializer = ProcedureStepSerializer(procedure_steps_model , many = True)

        return Response({"response" : procedure_steps_serializer.data})
    


    def post(self , request):
        procedure_step_serializer = ProcedureStepSerializer(data = request.data)

        if procedure_step_serializer.is_valid():
            procedure_step_serializer.save()
            return Response({"response" : procedure_step_serializer.data} , status=status.HTTP_201_CREATED)
        
        return Response({"response" : procedure_step_serializer.errors} , status = status.HTTP_400_BAD_REQUEST)