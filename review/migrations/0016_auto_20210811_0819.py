# Generated by Django 3.0.14 on 2021-08-11 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0015_auto_20210811_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
