# Generated by Django 4.1.5 on 2023-01-04 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperequirement',
            name='quantity',
            field=models.FloatField(default=0),
        ),
    ]
