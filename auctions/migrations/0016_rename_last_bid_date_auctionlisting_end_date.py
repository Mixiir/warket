# Generated by Django 4.1 on 2022-09-06 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auctionlisting_auction_period'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionlisting',
            old_name='last_bid_date',
            new_name='end_date',
        ),
    ]
