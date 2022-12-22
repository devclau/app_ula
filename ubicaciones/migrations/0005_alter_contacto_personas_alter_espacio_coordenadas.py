# Generated by Django 4.1.3 on 2022-12-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubicaciones', '0004_alter_sede_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='personas',
            field=models.TextField(verbose_name='Personas (nombre,cargo, email,fonos)'),
        ),
        migrations.AlterField(
            model_name='espacio',
            name='coordenadas',
            field=models.CharField(max_length=250, verbose_name='Coordenadas (Longitud , Latitud)'),
        ),
    ]