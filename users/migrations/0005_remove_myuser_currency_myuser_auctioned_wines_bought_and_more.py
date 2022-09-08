# Generated by Django 4.1.1 on 2022-09-08 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_myuser_auction_limit_myuser_auctioneer_myuser_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='currency',
        ),
        migrations.AddField(
            model_name='myuser',
            name='auctioned_wines_bought',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='auctioned_wines_sold',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='bought_wines',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='sold_wines',
            field=models.PositiveIntegerField(default=0),
        ),
    ]