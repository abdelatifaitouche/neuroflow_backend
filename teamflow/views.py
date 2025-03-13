from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import *
from .serializer import ProcessSerializer
from rest_framework import status


class ProcessListView(APIView):
    def get(self, request):
        process_list = Process.objects.all()
        process_list_serializer = ProcessSerializer(process_list , many = True)
        return Response({'response' : process_list_serializer.data} , status=status.HTTP_200_OK)
    

    def post(self , request):
        
        data = request.data
        process_serializer = ProcessSerializer(data = data)
        if process_serializer.is_valid():
            process_serializer.save()
            return Response({'response' : process_serializer.data} , status = status.HTTP_201_CREATED)


        return Response({'response' : process_serializer.errors} , status = status.HTTP_400_BAD_REQUEST)
