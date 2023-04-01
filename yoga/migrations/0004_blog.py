# Generated by Django 4.0.5 on 2023-03-28 16:48

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0003_slider_discount_alter_slider_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d', verbose_name='Resim : (370x240)')),
                ('list', models.ImageField(blank=True, upload_to='products/%y/%m/%d', verbose_name='Resim : (1170x714)')),
                ('title', models.CharField(default='Title', max_length=1000)),
                ('info', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]