"""
URL configuration for neuroflow_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from rest_framework_simplejwt.views import TokenVerifyView , TokenRefreshView
from user_management.views import CustomTokenObtainView ,VerifyAuthView , LogoutView , DepartementViewList , ProfileViewDetail , UsersViewList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', CustomTokenObtainView.as_view(), name='token_obtain_pair'),
    path('api/auth/verify/' , VerifyAuthView.as_view() , name='auth verify'),
    path('api/auth/logout/' ,LogoutView.as_view() , name="logout" ),
    path('api/auth/profile/' , ProfileViewDetail.as_view() , name="profile" ),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/users_list/' , UsersViewList.as_view() , name="users"),

    path('api/departements/departements_list' , DepartementViewList.as_view() , name="departements"),
    path("api/procedures/" , include("procedureflow.urls")),
    path('api/teamflow/' , include('teamflow.urls'))
]