from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsync_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='descricao',
        ),
    ]
