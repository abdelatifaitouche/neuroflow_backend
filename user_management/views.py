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

"""
class VerifyAuthView(TokenVerifyView):
    def post(self , request , *args , **kwargs):
        access_token = request.COOKIES.get("access_token")

        if access_token : 

            data = request.data.copy()

            data['token'] = access_token

            request._full_data = data

        response  = super().post(request , *args , **kwargs)
        return response
"""

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


"""
class LogoutView(APIView) : 
    def post(self , request , *args , **kwargs):

        response = JsonResponse({'detail': 'Logged out successfully'})

        response.set_cookie(
            key = 'access_token',  # Name of the cookie to delete
            value = '',  # Clear the cookie value
            expires=datetime.now() - timedelta(days=1),  # Set expiration in the past
            httponly=True, 
            secure=True, 
            samesite='Strict',  # Match the attributes of the original cookie
            path='/'
        )

        return response
"""


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