from django.urls import path
from teamflow.views import * 

urlpatterns = [
    path('process/' , ProcessListView.as_view()),
]