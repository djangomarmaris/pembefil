# Generated by Django 3.0.5 on 2021-08-08 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_image5'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='noDropDown',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
