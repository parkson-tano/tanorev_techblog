# Generated by Django 3.0.14 on 2021-08-11 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0018_auto_20210811_0822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='content',
        ),
    ]
