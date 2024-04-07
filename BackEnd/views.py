
from BackEnd.models import Ticket,TicketAtualizacao
from BackEnd.serializer import TicketSerializer,TicketAtualizacaoSerializer

from rest_framework import permissions


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import  DjangoModelPermissionsOrAnonReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import BasePermission

class AdminOnlyPermission(BasePermission):
    """
    Permite apenas que os administradores realizem operações de criação, atualização e exclusão.
    """
    def has_permission(self, request, view):
        # Apenas permitir se o usuário for um administrador e estiver autenticado
        return request.user and request.user.is_authenticated and request.user.is_staff

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user)
        return request.user


class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    http_method_names = ['get', 'post', 'put', 'patch','delete']


class TicketAtualizacaoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    queryset = TicketAtualizacao.objects.all()
    serializer_class = TicketAtualizacaoSerializer
    http_method_names = ['get', 'post', 'put', 'patch','delete']