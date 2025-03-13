from django.urls import path
from teamflow.views import * 

urlpatterns = [
    path('' , ProcessListView.as_view()),
]