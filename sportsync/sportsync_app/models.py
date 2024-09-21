import uuid
from django.db import models

class Endereco(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.cidade}, {self.estado}"

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    senha_hash = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class Esporte(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    max_participantes = models.IntegerField()
    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Partida(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE)

class Quadra(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class UsuarioPartida(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('partida', 'usuario')

class UsuarioEvento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'evento')
