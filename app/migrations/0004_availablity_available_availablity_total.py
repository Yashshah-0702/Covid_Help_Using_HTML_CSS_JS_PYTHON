# Generated by Django 4.1.2 on 2022-10-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_availablity'),
    ]

    operations = [
        migrations.AddField(
            model_name='availablity',
            name='available',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='availablity',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
