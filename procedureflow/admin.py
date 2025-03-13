from django.contrib import admin
from .models import Procedure, ProcedureStep
#from .models import Process
# Register your models here.



admin.site.register(Procedure)
admin.site.register(ProcedureStep)
#admin.site.register(Process)
