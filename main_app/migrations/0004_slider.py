# Generated by Django 3.1.7 on 2021-03-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_setting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=700)),
                ('sliders_img', models.ImageField(upload_to='sliders/')),
            ],
        ),
    ]