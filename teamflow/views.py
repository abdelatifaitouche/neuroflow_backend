from django.shortcuts import render , get_object_or_404
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



class ProcessDetailView(APIView):

    def get(self, request, pk):
        process = get_object_or_404(Process, pk=pk)
        serializer = ProcessSerializer(process)
        return Response({'response': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        process = get_object_or_404(Process, pk=pk)
        serializer = ProcessSerializer(process, data=request.data)  # Full update
        if serializer.is_valid():
            serializer.save()
            return Response({'response': serializer.data}, status=status.HTTP_200_OK)
        return Response({'response': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        process = get_object_or_404(Process, pk=pk)
        serializer = ProcessSerializer(process, data=request.data, partial=True)  # Partial update
        if serializer.is_valid():
            serializer.save()
            return Response({'response': serializer.data}, status=status.HTTP_200_OK)
        return Response({'response': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        process = get_object_or_404(Process, pk=pk)
        process.delete()
        return Response({'response': "deleted"}, status=status.HTTP_204_NO_CONTENT)
