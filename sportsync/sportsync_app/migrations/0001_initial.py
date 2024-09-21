import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('pais', models.CharField(max_length=255)),
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
            name='Evento',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('max_participantes', models.IntegerField()),
                ('esporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsync_app.esporte')),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('esporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsync_app.esporte')),
            ],
        ),
        migrations.CreateModel(
            name='Quadra',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsync_app.evento')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('senha_hash', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('telefone', models.CharField(max_length=20)),
                ('data_nascimento', models.DateField()),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportsync_app.endereco')),
            ],
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
