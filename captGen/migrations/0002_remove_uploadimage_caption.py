# Generated by Django 4.2 on 2023-05-12 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('captGen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadimage',
            name='caption',
        ),
    ]
