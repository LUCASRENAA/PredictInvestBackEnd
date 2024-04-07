from rest_framework import serializers
from BackEnd.models import   Ticket,TicketAtualizacao




class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketAtualizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketAtualizacao
        fields = '__all__'