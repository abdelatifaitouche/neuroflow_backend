from django.urls import path
from teamflow.views import * 

urlpatterns = [
    path('process/' , ProcessListView.as_view()),
    path('process/process_details/<int:pk>' , ProcessDetailView.as_view())
]