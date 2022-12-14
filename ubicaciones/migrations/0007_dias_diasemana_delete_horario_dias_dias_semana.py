# Generated by Django 4.1.3 on 2022-12-16 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubicaciones', '0006_horario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DiaSemana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Dia de la Semana')),
            ],
        ),
        migrations.DeleteModel(
            name='Horario',
        ),
        migrations.AddField(
            model_name='dias',
            name='dias_semana',
            field=models.ManyToManyField(to='ubicaciones.diasemana'),
        ),
    ]
