from rest_framework import serializers
from BackEnd.models import   Ticket,TicketAtualizacao

from decimal import Decimal



class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketAtualizacaoSerializer(serializers.ModelSerializer):
    ticket_id = serializers.CharField(source='ticket.id', read_only=True)
    name = serializers.CharField(source='ticket.name', read_only=True)  # aqui é o nome do ticket
    
    class Meta:
        
        model = TicketAtualizacao
        fields = '__all__'
    