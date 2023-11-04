from rest_framework import routers
from django.urls import path
from .api.api import *

rutas = routers.DefaultRouter()
#Ruta para servicios
rutas.register(r'servicios',ServcioViewSet,'Servicios')

#Ruta para Equipos
rutas.register(r'equipo',EquipoViewSet,'Equipo')

#Ruta para Hallazgos
rutas.register(r'hallazgo',HallazgoViewSet,'hallazgo')

#Ruta para Diagnosticos
rutas.register(r'diagnostico',DiagnosticoViewSet,'diagnostico')


urlpatterns=[

    #Rutas para servicio
    path('servicios/get-folio', get_folio, name='get-folio'),
    path('servicios/detail/<int:pk>/', servicio_detail, name='servicio-detail'),
    path('servicios/<int:pk>/update-date/', update_date, name='update-date'),
    path('servicios/<int:pk>/update-etapa/',update_etapa,name='update-etapa'),
    
    
    #Rutas para Equipo

]

urlpatterns += rutas.urls