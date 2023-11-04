from rest_framework import viewsets,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from datetime import datetime

from  ..serializers import *
from ..models import Servicio, Etapa,Equipo,Hallazgo,Diagnostico




#Servico
class ServcioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

@api_view(['GET'])
def servicio_detail(request,pk):
    try:
        servicio = Servicio.objects.get(pk=pk)
        equipo = Equipo.objects.get(servicio= servicio)
        hallazgo = Hallazgo.objects.filter(servicio=servicio)

        hallazgos = []
        

        for i in hallazgo.all():
            diagnostico = []
            diagnosticos = Diagnostico.objects.filter(hallazgo=i)
            for j in diagnosticos.all():
                diagnostico.append({
                    'id':j.id,
                    'nombre':j.nombre,
                    #'foto_pieza':j.foto_pieza,
                    'tiempo_intalacion': j.tiempo_instalacion,
                    'recomendacion':j.recomendacion,
                    'costo':j.costo,
                    'descripcion':j.descripcion
                })

            hallazgos.append({
                'id':i.id,
                'nombre': i.nombre,
                'descripcion': i.descripcion,
                'diagnosticos': diagnostico
            })


        data = {
            'servicio' : ServicioSerializer(servicio).data,
            'equipo': EquipoSerializer(equipo).data,
            'hallazgos':hallazgos
        }
        return Response(data)
    
    except (Servicio.DoesNotExist,Equipo.DoesNotExist):
        return Response({'msg':'Servicio no encontrado'},status=status.HTTP_404_NOT_FOUND)


@api_view(['PACTH','PUT'])
def update_date(request,pk):
    try:
        servicio = Servicio.objects.get(pk=pk)
        costo_final = request.data.get('costo_final')

        fecha_entrega = request.data.get('fecha_entrega')

        if fecha_entrega is not None:
            servicio.fecha_entrega = fecha_entrega
            servicio.save()
            data = ServicioSerializer(servicio)
        else:
            return Response({'msg':'El campo es requerido'},status=status.HTTP_400_BAD_REQUEST)
    
        return Response(data.data)
    
    except Servicio.DoesNotExist:
        return Response({'msg':'Servicio no encontrado'},status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_etapa(request,pk):
    try:
        id_etapa = request.data.get('id_etapa')
        servicio = Servicio.objects.get(pk=pk)

        if id_etapa is not None:
            etapa = Etapa.objects.get(pk=id_etapa)
            servicio.etapa = etapa
            servicio.save()
            data = ServicioSerializer(servicio)
            return Response(data.data)
    except (Servicio.DoesNotExist, Etapa.DoesNotExist):
        return Response({'msg':'Servicio o etapa no encontrado'},status=status.HTTP_404_NOT_FOUND)


#Equipo 
class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

#Hallazgo
class HallazgoViewSet(viewsets.ModelViewSet):
    queryset = Hallazgo.objects.all()
    serializer_class = HallazgoSerializer

#Diagnostico
class DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer



@api_view(['GET'])
def get_folio(request):
    count = f"{Servicio.objects.count() + 1}"
    now = datetime.now()
    folio = f'CP-{now.strftime("%y")}-{now.month}-'
    str_len = len(count)
    for _ in range(5-str_len): folio+='0'
    folio+=f'{count}'
    return Response({'folio':folio})






