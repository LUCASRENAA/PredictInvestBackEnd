# Generated by Django 4.2.9 on 2024-04-06 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0002_ticketatualizacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='name',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]
