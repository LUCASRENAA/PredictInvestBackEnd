from rest_framework import serializers
from BackEnd.models import   Ticket




class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'