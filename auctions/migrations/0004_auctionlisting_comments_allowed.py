# Generated by Django 4.1 on 2022-09-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_auctionlisting_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='comments_allowed',
            field=models.BooleanField(default=True),
        ),
    ]
