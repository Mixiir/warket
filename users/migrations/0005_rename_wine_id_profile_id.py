# Generated by Django 4.1 on 2022-09-06 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_birth_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='id',
            new_name='id',
        ),
    ]
