# Generated by Django 4.0.5 on 2023-03-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_remove_reservation_adress_reservation_adres_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='price',
            field=models.CharField(db_index=True, default='Price', max_length=100, null=True),
        ),
    ]
