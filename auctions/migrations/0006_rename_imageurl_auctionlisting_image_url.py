# Generated by Django 4.1 on 2022-09-06 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_rename_comments_allowed_auctionlisting_commentsallowed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionlisting',
            old_name='imageUrl',
            new_name='image_url',
        ),
    ]
