# Generated by Django 3.2 on 2023-04-24 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20230425_0236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='habits',
            new_name='habit',
        ),
    ]
