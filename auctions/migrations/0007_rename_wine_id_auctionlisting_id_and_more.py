# Generated by Django 4.1 on 2022-09-06 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_rename_imageurl_auctionlisting_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='bidValue',
            new_name='bid_value',
        ),
    ]
