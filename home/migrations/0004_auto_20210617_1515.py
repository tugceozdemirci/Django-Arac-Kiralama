# Generated by Django 3.1.7 on 2021-06-17 12:15

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contactformmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='about',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='contact',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='references',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
