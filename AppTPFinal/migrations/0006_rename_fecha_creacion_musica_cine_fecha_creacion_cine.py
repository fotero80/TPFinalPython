# Generated by Django 4.1 on 2022-09-09 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTPFinal', '0005_remove_cine_email_usuario_cine_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cine',
            old_name='fecha_creacion_musica',
            new_name='fecha_creacion_cine',
        ),
    ]