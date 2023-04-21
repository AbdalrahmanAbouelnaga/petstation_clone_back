# Generated by Django 4.2 on 2023-04-14 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productvariant',
            old_name='title',
            new_name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]