# Generated by Django 4.1 on 2022-08-31 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warket_viewer', '0017_remove_cart_total_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]