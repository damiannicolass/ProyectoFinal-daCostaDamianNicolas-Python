# Generated by Django 5.0.6 on 2024-08-07 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspecciones', '0003_alter_inspeccion_enlace_unico'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspeccion',
            name='fotos_subidas',
            field=models.BooleanField(default=False),
        ),
    ]
