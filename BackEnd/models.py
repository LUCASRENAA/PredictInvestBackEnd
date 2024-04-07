from django.contrib.auth.models import User
from django.db import models




class Ticket(models.Model):
    ticket = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class TicketAtualizacao(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='atualizacoes' , on_delete=models.CASCADE)
    data_atualizacao = models.DateTimeField(auto_now=True)
    valor_atual = models.DecimalField(max_digits=10, decimal_places=5,default=0)
    payout = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    lpa = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    vpa = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    pl = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    pvp = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    psr = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    roe = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    roa = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    EBITDA = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    margem_bruta = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    margem_liquida = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    margem_ebitda = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    margem_operacional = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    pcf = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    liquidez_corrente = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    liquidez_imediata = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    liquidez_seca = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    giro_ativo = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    endividamento_geral = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    ativo_acao = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    divida_bruta = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    divida_liquida = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    capital_giro = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    receita_liquida = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    ebit_acao = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    margem_ebit =models.DecimalField(max_digits=10, decimal_places=2,default=0)
    grahan =models.DecimalField(max_digits=10, decimal_places=2,default=0)
    bazin = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        return self.ticket.ticket
