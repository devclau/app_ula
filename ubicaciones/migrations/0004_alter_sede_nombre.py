# Generated by Django 4.1.3 on 2022-12-16 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubicaciones', '0003_alter_espacio_options_remove_reparticionespacio_uso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sede',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre Sede'),
        ),
    ]
