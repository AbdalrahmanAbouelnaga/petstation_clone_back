# Generated by Django 4.2 on 2023-04-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_brand_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]