# Generated by Django 4.2.7 on 2023-11-13 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CloudParkApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='rules',
            field=models.ManyToManyField(blank=True, to='CloudParkApp.contractrule'),
        ),
    ]
