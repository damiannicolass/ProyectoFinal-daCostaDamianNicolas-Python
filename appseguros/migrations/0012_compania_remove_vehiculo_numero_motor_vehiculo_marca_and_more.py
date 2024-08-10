# Generated by Django 5.0.6 on 2024-07-31 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appseguros', '0011_siniestro_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='numero_motor',
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='version',
            field=models.CharField(default='desconocido', max_length=30),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_poliza', models.CharField(max_length=20)),
                ('tipo_seguro', models.CharField(choices=[('moto', 'Moto'), ('auto', 'Auto'), ('bici', 'Bicicleta'), ('combinado_familiar', 'Combinado Familiar'), ('otros', 'Otros')], max_length=20)),
                ('ramo_otros', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField()),
                ('estado_poliza', models.CharField(max_length=20)),
                ('es_vehiculo', models.BooleanField(default=False)),
                ('informacion_adicional', models.TextField(blank=True, null=True)),
                ('asegurado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appseguros.asegurado')),
                ('compania', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appseguros.compania')),
                ('vehiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appseguros.vehiculo')),
            ],
        ),
    ]
