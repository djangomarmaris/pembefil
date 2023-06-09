# Generated by Django 4.0.5 on 2023-03-29 18:59

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0007_blog_mini_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=1000)),
                ('info', ckeditor_uploader.fields.RichTextUploadingField()),
                ('title_two', models.CharField(default='Title', max_length=1000)),
                ('info_two', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(blank=True, upload_to='products/%y/%m/%d', verbose_name='Resim : (370x610)')),
            ],
        ),
    ]
