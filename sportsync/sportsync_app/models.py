import uuid
from django.db import models

class Endereco(models.Model):
    id_endereco = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.cidade}, {self.estado}"

class Usuario(models.Model):
    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Esporte(models.Model):
    id_esporte = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    id_evento = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    max_participantes = models.IntegerField()
    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Partida(models.Model):
    id_partida = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Quadra(models.Model):
    id_quadra = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE)
    disponibilidade = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
