# Generated by Django 4.0.5 on 2023-03-17 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_category_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='bestsale',
            new_name='list',
        ),
    ]