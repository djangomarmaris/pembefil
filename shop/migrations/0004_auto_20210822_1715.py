# Generated by Django 3.0.5 on 2021-08-22 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_nodropdown'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image5',
        ),
    ]