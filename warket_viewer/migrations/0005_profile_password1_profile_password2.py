# Generated by Django 4.1 on 2022-08-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warket_viewer', '0004_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='password2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]