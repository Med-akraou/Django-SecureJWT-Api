# Generated by Django 4.1.2 on 2022-10-22 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='matricule',
        ),
        migrations.RemoveField(
            model_name='user',
            name='raisonsociale',
        ),
    ]