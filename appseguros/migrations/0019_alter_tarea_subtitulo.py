# Generated by Django 5.0.6 on 2024-08-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appseguros', '0018_siniestro_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
