# Generated by Django 4.2 on 2023-04-13 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
        ('products', '0004_remove_category_image_animal_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='homepage.brand'),
            preserve_default=False,
        ),
    ]
