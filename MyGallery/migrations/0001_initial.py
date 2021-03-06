# Generated by Django 3.2.9 on 2021-12-01 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='photos/')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('category', models.ManyToManyField(to='MyGallery.Category')),
                ('location', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MyGallery.location')),
            ],
        ),
    ]
