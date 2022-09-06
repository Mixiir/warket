# Generated by Django 4.1 on 2022-09-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auctionlisting_current_maximum_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='current_maximum_bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
