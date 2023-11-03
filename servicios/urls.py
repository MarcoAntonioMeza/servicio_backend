from rest_framework import routers
from django.urls import path
from .api.api import ServcioViewSet, get_folio,update_date,update_etapa

rutas = routers.DefaultRouter()
rutas.register(r'servicios',ServcioViewSet,'Servicios')

urlpatterns=[
    
    path('servicios/get-folio', get_folio, name='get-folio'),
    path('servicios/<int:pk>/update-date/', update_date, name='update-date'),
    path('servicios/<int:pk>/update-etapa/',update_etapa,name='update-etapa'),
]

urlpatterns += rutas.urls