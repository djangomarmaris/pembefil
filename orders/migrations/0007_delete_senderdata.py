# Generated by Django 4.0.5 on 2022-07-14 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_senderdata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SenderData',
        ),
    ]
