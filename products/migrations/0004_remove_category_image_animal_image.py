# Generated by Django 4.2 on 2023-04-13 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]
