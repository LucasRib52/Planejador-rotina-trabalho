# planejador/models.py

from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data = models.DateField()
    hora = models.TimeField()
    realizado = models.BooleanField(default=False)
    descricao_execucao = models.TextField(blank=True)
    hora_finalizacao = models.TimeField(blank=True, null=True)
    motivo_nao_finalizado = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.data} {self.hora}"
