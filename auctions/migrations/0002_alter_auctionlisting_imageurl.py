# Generated by Django 4.1 on 2022-08-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='imageUrl',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='images'),
        ),
    ]