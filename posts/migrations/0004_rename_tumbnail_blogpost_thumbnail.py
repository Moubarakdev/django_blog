# Generated by Django 4.0.6 on 2022-07-20 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_blogpost_tumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='tumbnail',
            new_name='thumbnail',
        ),
    ]
