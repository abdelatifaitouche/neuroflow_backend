from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView , TokenVerifyView
from rest_framework.views import APIView
# Create your views here.
from django.conf import settings
from django.http import JsonResponse
from datetime import datetime , timedelta
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from user_management.authenticate import CustomAuthentication

from user_management.models import Departement
from user_management.serializers import DepartementSerializer , CustomUserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

from user_management.models import CustomUser


class CustomTokenObtainView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        access_token = response.data['access']
        refresh_token = response.data['refresh']
        response.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_COOKIE'] ,
            value=access_token , 
            domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"],
            path=settings.SIMPLE_JWT["AUTH_COOKIE_PATH"],
            expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
            secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
        )

        response.set_cookie(
            key='refresh_token',
            value=refresh_token,
            httponly=True,
            secure=True,
            samesite='Strict',
            path='/'
        )

        return response

class VerifyAuthView(TokenVerifyView):

    authentication_classes = [CustomAuthentication]

    def post(self, request, *args, **kwargs):
        access_token = request.COOKIES.get("access_token")

        if not access_token:
            return Response({"detail": "No access token provided"}, status=status.HTTP_401_UNAUTHORIZED)

        # Manually pass token data to the serializer
        data = {"token": access_token}


        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            return Response({"detail": "Token is valid"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView): 

    authentication_classes = [CustomAuthentication]

    def post(self, request, *args, **kwargs):
        response = JsonResponse({'detail': 'Logged out successfully'})
        print(request.COOKIES.get('access_token'))

        token = RefreshToken(request.COOKIES.get("refresh_token"))
        token.blacklist()

        # Properly expire the cookie
        response.delete_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            path=settings.SIMPLE_JWT["AUTH_COOKIE_PATH"],
            domain=settings.SIMPLE_JWT["AUTH_COOKIE_DOMAIN"]
        )   

        response.delete_cookie(
            key='refresh_token',
            path='/',  # Ensure it's the same path as when it was set
            samesite='Strict',
        )   

        response.set_cookie(
            key='access_token',
            value='',
            expires='Thu, 01 Jan 1970 00:00:00 GMT',  # Expire immediately
            path='/',
            httponly=True,
            secure=True,
            samesite='None',
            )

        response.set_cookie(
            key='refresh_token',
            value='',
            expires='Thu, 01 Jan 1970 00:00:00 GMT',
            path='/',
            httponly=True,
            secure=True,
            samesite='None',
            )


        return response
    




#api/auth/profile GET ---> validate the token ---> return a user


class ProfileViewDetail(APIView):

    authentication_classes = [CustomAuthentication]

    def get(self , request):

        access_token = request.COOKIES.get("access_token")

        user_id = AccessToken(access_token , True)['user_id'] #extract the user id from the access token

        current_user = CustomUser.objects.get(id = user_id)

        current_user_Serializer = CustomUserSerializer(current_user , many = False)
        
        return Response({'profileData' : current_user_Serializer.data} , status=status.HTTP_200_OK)





class DepartementViewList(APIView):
    authentication_classes = [CustomAuthentication]

    def get(self , request):

        departements_data = Departement.objects.all()

        departement_serializer = DepartementSerializer(departements_data , many  = True)

        return Response({"departements" : departement_serializer.data} , status= status.HTTP_200_OK)
    


class UsersViewList(APIView):
    
    authentication_classes = [CustomAuthentication]
    def get(self , request):

        users = CustomUser.objects.all()

        user_serializer = CustomUserSerializer(users , many = True)

        return Response({"users" : user_serializer.data})
