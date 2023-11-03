from rest_framework import serializers
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer
from .models import Servicio,Equipo,Hallazgo,Diagnostico,Etapa



class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('__all__')

        read_only_fields = ('folio','etapa')

    def to_representation(self, instance):

        users = []
        for user in instance.usuario.all():
            users.append({
                'id': user.id,
                'nombre':user.full_name,
                'tipo': user.tipo
            })

        return{
            'id':instance.id,
            'folio':instance.folio,
            'descripcion_cliente':instance.descripcion_cliente,
            'fecha_recibo': instance.fecha_recibo,
            'costo_aproximado':instance.costo_aproximado,
            'costo_final':instance.costo_final,
            'fecha_entrega':instance.fecha_entrega,

            'usuarios':users,
            'etapa':{
                'id':instance.etapa.id,
                'nombre':instance.etapa.nombre
            }
        }
