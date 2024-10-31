import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cep', models.CharField(max_length=10)),
                ('rua', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Esporte',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Quadra',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('disponibilidade', models.BooleanField(default=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportsync_app.endereco')),
                ('esportes', models.ManyToManyField(related_name='quadras', to='sportsync_app.esporte')),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('descricao', models.TextField()),
                ('data', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('horario_fim', models.TimeField()),
                ('max_participantes', models.IntegerField()),
                ('curtidas', models.ManyToManyField(blank=True, related_name='partidas_curtidas', to=settings.AUTH_USER_MODEL)),
                ('esporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsync_app.esporte')),
                ('organizador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partidas', to=settings.AUTH_USER_MODEL)),
                ('quadra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportsync_app.quadra')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioPartida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsync_app.partida')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('partida', 'usuario')},
            },
        ),
        migrations.AddField(
            model_name='partida',
            name='usuarios',
            field=models.ManyToManyField(related_name='partidas_jogadas', through='sportsync_app.UsuarioPartida', to=settings.AUTH_USER_MODEL),
        ),
    ]
