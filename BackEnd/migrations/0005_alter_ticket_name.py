# Generated by Django 5.2 on 2025-04-24 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0004_ticket_ticket_id_alter_ticket_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
