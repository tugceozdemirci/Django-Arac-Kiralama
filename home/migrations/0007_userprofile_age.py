# Generated by Django 3.1.7 on 2021-06-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210629_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]