# Generated by Django 4.1 on 2022-09-09 00:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppTPFinal', '0002_literatura_fecha_creacion_literatura'),
    ]

    operations = [
        migrations.AddField(
            model_name='cine',
            name='fecha_creacion_musica',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musica',
            name='fecha_creacion_musica',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='fecha_creacion_usuario',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
