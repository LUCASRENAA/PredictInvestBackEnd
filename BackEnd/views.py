
from BackEnd.models import Ticket,TicketAtualizacao
from BackEnd.serializer import TicketSerializer,TicketAtualizacaoSerializer

from rest_framework import permissions


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import  DjangoModelPermissionsOrAnonReadOnly

from rest_framework import viewsets


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user)
        return request.user


class TicketViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, UserPermission]

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    http_method_names = ['get', 'post', 'put', 'path','delete']


class TicketAtualizacaoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, UserPermission]

    queryset = TicketAtualizacao.objects.all()
    serializer_class = TicketAtualizacaoSerializer
    http_method_names = ['get', 'post', 'put', 'path','delete']