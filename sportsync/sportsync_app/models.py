import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo de email deve ser preenchido.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'telefone']

    def __str__(self):
        return self.nome

class Esporte(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.cidade}, {self.estado}"

class Quadra(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    esportes = models.ManyToManyField(Esporte, related_name="quadras")
    disponibilidade = models.BooleanField(default=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.nome

class Partida(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, related_name="partidas")
    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    horario_fim = models.TimeField()
    quadra = models.ForeignKey(Quadra, on_delete=models.SET_NULL, null=True)
    max_participantes = models.IntegerField()
    usuarios = models.ManyToManyField(Usuario, through='UsuarioPartida', related_name='partidas_jogadas')
    curtidas = models.ManyToManyField(Usuario, related_name="partidas_curtidas", blank=True)

    def __str__(self):
        return f"Partida de {self.esporte.nome} em {self.quadra.nome} no dia {self.data}"

class UsuarioPartida(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('partida', 'usuario')
