# Generated by Django 3.1.7 on 2021-07-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_auto_20210701_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]
