# Generated by Django 4.0.5 on 2023-03-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0005_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d', verbose_name='Resim : (868x655)'),
        ),
    ]
