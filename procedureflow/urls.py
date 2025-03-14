


from django.urls import path , include
from .views import *


urlpatterns = [
    path('procedures_list/' , ProcedureListView.as_view()) , 
    path('procedure_details/<int:pk>' , ProcedureDetailView.as_view()),

    path("procedure/<int:pk>/steps" , ProcedureStepListView.as_view()),


    path('procedure/steps/<int:step_id>' , StepDetailView.as_view())

    #path('procedure/<int:pk>/export' , ExportToPdfView.as_view())
]