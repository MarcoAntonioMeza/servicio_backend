from rest_framework import serializers
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer
from .models import Servicio,Equipo,Hallazgo,Diagnostico,Etapa

#Serializer del modelo Equipo
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields =("__all__")
        read_only_fields = ('servicio','caracteristicas_reales')

    def to_representation(self,instance):
        
        return{
            'id':instance.id,
            'nombre':instance.nombre,
            'caracteristicas_posibles': instance.caracteristicas_posibles,
            'caracteristicas_reales': instance.caracteristicas_reales,
            'servicio':{
                'id':instance.servicio.id,
                'folio':instance.servicio.folio
            }
        }

#Serializer de hallazgo
class HallazgoSerializer(serializers.ModelSerializer):
    class Meta():
        model = Hallazgo
        fields = ('__all__')

#Serializer de Diagnosticos

class DiagnosticoSerializer(serializers.ModelSerializer):
    #hallazgo = HallazgoSerializer()
    class Meta:
        model = Diagnostico
        fields = ('__all__')

    

"""

Serializers del modelo servicio

"""
class ServicioSerializer(serializers.ModelSerializer):
    #equipo = EquipoSerializer()
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
            #'equipo':instance.equipo,

            'usuarios':users,
            'etapa':{
                'id':instance.etapa.id,
                'nombre':instance.etapa.nombre
            }
        }


    


