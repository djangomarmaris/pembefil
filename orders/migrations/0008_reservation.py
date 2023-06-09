# Generated by Django 4.0.5 on 2023-03-22 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_delete_senderdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, default='name', max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, db_index=True, default='Pickup', max_length=100, null=True)),
                ('tc', models.CharField(blank=True, db_index=True, default='Dropup', max_length=100, null=True)),
                ('phone', models.CharField(blank=True, db_index=True, default='ReturnDropup', max_length=100, null=True)),
                ('city', models.CharField(db_index=True, default='Name', max_length=100, null=True)),
                ('adress', models.CharField(db_index=True, default='Car', max_length=100, null=True)),
                ('email', models.CharField(db_index=True, default='Email', max_length=100, null=True)),
                ('tokenCheck', models.CharField(default=False, max_length=50, verbose_name='Token check:')),
                ('cardHolderName', models.CharField(blank=True, db_index=True, default='KK Sahibi', max_length=100, null=True)),
                ('cardNumber', models.CharField(blank=True, db_index=True, default='KK Number', max_length=100, null=True)),
                ('expireMonth', models.CharField(blank=True, db_index=True, default='Ay', max_length=100, null=True)),
                ('expireYear', models.CharField(blank=True, db_index=True, default='Yıl', max_length=100, null=True)),
                ('cvc', models.CharField(blank=True, db_index=True, default='CVC', max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
