from rest_framework import viewsets,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  ..serializers import ServicioSerializer

from datetime import datetime



from ..models import Servicio, Etapa

class ServcioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


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

def actualizar(model,serializer,instance_id, field, data)-> Response:
    try:
        modelo = model.objects.get(pk= instance_id)
        modelo.update(field = data)
        res = serializer(modelo)
        return Response(res.data)
    
    except modelo.DoesNotExist:
        return Response({'msg':'Servicio no encontrado'},status=status.HTTP_404_NOT_FOUND)






@api_view(['GET'])
def get_folio(request):
    count = f"{Servicio.objects.count() + 1}"
    now = datetime.now()
    folio=''
    str_len = len(count)
    folio += f'CP-{now.strftime("%y")}-{now.month}'
    for _ in range(5-str_len): folio+='0'
    folio+=f'{count}'
    return Response(folio)






