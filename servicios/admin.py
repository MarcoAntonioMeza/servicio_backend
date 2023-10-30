from django.contrib import admin
from .models import *

# Register your models here.

modelos = Etapa,Servicio,Hallazgo,Diagnostico,Equipo
admin.site.register(modelos)