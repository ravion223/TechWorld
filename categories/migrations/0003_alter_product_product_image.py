# Generated by Django 5.1 on 2024-10-07 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='no-image.jpg', upload_to='product/'),
        ),
    ]
