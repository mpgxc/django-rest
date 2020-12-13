from .serializers import (GroupSerializer, UserSerializer)
from django.contrib.auth.models import (Group, User)
from rest_framework import viewsets
from rest_framework import permissions


class UserViewrSet(viewsets.ModelViewSet):
    """
        Endpoint para acesso as Usuários (Listar, Editar, Deletar)
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
         Endpoint para acesso aos Grupos (Listar, Editar, Deletar)
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
