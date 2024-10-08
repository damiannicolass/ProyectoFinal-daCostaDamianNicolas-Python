# Generated by Django 5.0.6 on 2024-07-31 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appseguros', '0007_alter_comentario_texto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiculo',
            old_name='año',
            new_name='anio',
        ),
        migrations.AddField(
            model_name='asegurado',
            name='mail',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='asegurado',
            name='telefono',
            field=models.CharField(default=0, max_length=18),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='siniestro',
            name='asegurado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appseguros.asegurado'),
        ),
    ]
