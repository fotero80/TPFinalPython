# Generated by Django 4.1 on 2022-09-15 21:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id_mensaje', models.AutoField(primary_key=True, serialize=False)),
                ('usuario_origen', models.CharField(max_length=50)),
                ('usuario_destino', models.CharField(max_length=50)),
                ('mensaje', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('fecha_creacion_mensaje', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
