from rest_framework import viewsets,permissions

from rest_framework.response import Response

from usuarios.serializers import UsuarioSerializer
from usuarios.models import Usuario

class UsuarioViewSet(viewsets.ModelViewSet):
    
    queryset = Usuario.objects.all()

    #permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [permissions.AllowAny]