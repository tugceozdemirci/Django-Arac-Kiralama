# Generated by Django 3.1.7 on 2021-07-01 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_reservation_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
