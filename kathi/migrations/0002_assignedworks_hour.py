# Generated by Django 3.0.3 on 2020-05-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kathi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedworks',
            name='hour',
            field=models.IntegerField(default=0),
        ),
    ]
