# Generated by Django 5.1 on 2024-10-16 23:30

import django.db.models.deletion
import uuid
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
                ('id_endereco', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cep', models.CharField(max_length=10)),
                ('rua', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Esporte',
            fields=[
                ('id_esporte', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id_evento', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('max_participantes', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportsync_app.endereco')),
                ('esporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsync_app.esporte')),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id_partida', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportsync_app.endereco')),
                ('evento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sportsync_app.evento')),
            ],
        ),
        migrations.CreateModel(
            name='Quadra',
            fields=[
                ('id_quadra', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('disponibilidade', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportsync_app.endereco')),
                ('esporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsync_app.esporte')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id_usuario', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='usuario_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='usuario_user_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='evento',
            name='organizador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sportsync_app.usuario'),
        ),
        migrations.CreateModel(
            name='UsuarioEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsync_app.evento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsync_app.usuario')),
            ],
            options={
                'unique_together': {('usuario', 'evento')},
            },
        ),
        migrations.CreateModel(
            name='UsuarioPartida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsync_app.partida')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsync_app.usuario')),
            ],
            options={
                'unique_together': {('partida', 'usuario')},
            },
        ),
    ]
