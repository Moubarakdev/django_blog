# Generated by Django 4.0.6 on 2022-07-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_blogpost_tumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='tumbnail',
            field=models.ImageField(blank=True, upload_to='blog'),
        ),
    ]
