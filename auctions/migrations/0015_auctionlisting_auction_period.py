# Generated by Django 4.1 on 2022-09-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auctionlisting_last_bidder'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='auction_period',
            field=models.PositiveIntegerField(default=10),
        ),
    ]