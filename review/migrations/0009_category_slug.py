# Generated by Django 3.1.5 on 2021-07-18 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0008_post_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
