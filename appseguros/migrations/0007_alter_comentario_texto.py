# Generated by Django 5.0.6 on 2024-07-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appseguros', '0006_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='texto',
            field=models.CharField(max_length=2000),
        ),
    ]
