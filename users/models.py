from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateTimeField('data do evento')
    descricao = models.TextField(blank=True, null=True)  # Adicionando o campo descricao

    def __str__(self):
        return self.nome
