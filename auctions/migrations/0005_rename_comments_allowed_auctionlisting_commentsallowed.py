# Generated by Django 4.1 on 2022-09-03 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auctionlisting_comments_allowed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionlisting',
            old_name='comments_allowed',
            new_name='comments_allowed',
        ),
    ]
