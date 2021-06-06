# Generated by Django 3.1.7 on 2021-06-06 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='parent_id',
            new_name='parent',
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('False', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('keywords', models.CharField(max_length=260)),
                ('description', models.CharField(blank=True, max_length=260)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('brand', models.CharField(max_length=15)),
                ('year', models.IntegerField()),
                ('vites', models.CharField(max_length=10)),
                ('price', models.FloatField()),
                ('fuel', models.CharField(max_length=260)),
                ('engine', models.CharField(max_length=260)),
                ('color', models.CharField(max_length=20)),
                ('seats', models.IntegerField()),
                ('luggage', models.CharField(max_length=10)),
                ('detail', models.TextField()),
                ('status', models.CharField(choices=[('False', 'Hayır'), ('True', 'Evet')], max_length=10)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.category')),
            ],
        ),
    ]
