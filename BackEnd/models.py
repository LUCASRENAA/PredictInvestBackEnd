from django.contrib.auth.models import User
from django.db import models




class Ticket(models.Model):
    name = models.CharField(max_length=5)
    setor = models.CharField(max_length=50)

    def __str__(self):
        return self.name
"""
class Ticket_Atualizacao(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='ticket' , on_delete=models.CASCADE)
    data_atualizacao = models.CharField(max_length=50)
    valor_atual = models.CharField(max_length=50)
    payout = models.CharField(max_length=50)
    lpa = models.CharField(max_length=50)
    vpa = models.CharField(max_length=50)
    pl = models.CharField(max_length=50)
    pvp = models.CharField(max_length=50)
    psr = models.CharField(max_length=50)
    roe = models.CharField(max_length=50)
    roa = models.CharField(max_length=50)
    EBITDA = models.CharField(max_length=50)
    margem_bruta = models.CharField(max_length=50)
    margem_liquida = models.CharField(max_length=50)
    margem_ebitda = models.CharField(max_length=50)
    margem_operacional = models.CharField(max_length=50)
    pcf = models.CharField(max_length=50)
    liquidez_corrente = models.CharField(max_length=50)
    liquidez_imediata = models.CharField(max_length=50)
    liquidez_seca = models.CharField(max_length=50)
    giro_ativo = models.CharField(max_length=50)
    endividamento_geral = models.CharField(max_length=50)
    ativo_acao = models.CharField(max_length=50)
    divida_bruta = models.CharField(max_length=50)
    divida_liquida = models.CharField(max_length=50)
    capital_giro = models.CharField(max_length=50)
    receita_liquida = models.CharField(max_length=50)
    ebit_acao = models.CharField(max_length=50)
    margem_ebit = models.CharField(max_length=50)
    grahan = models.CharField(max_length=50)
    bazin = models.CharField(max_length=50)

    def __str__(self):
        return self.ticket.name
"""