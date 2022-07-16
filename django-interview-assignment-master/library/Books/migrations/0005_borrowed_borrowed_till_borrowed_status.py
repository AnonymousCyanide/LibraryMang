# Generated by Django 4.0.6 on 2022-07-16 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0004_borrowed'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowed',
            name='borrowed_till',
            field=models.DateTimeField(default=datetime.date(2022, 7, 24)),
        ),
        migrations.AddField(
            model_name='borrowed',
            name='status',
            field=models.CharField(choices=[('Borrowed', 'Borrowed'), ('Returned', 'Returned')], default='Borrowed', max_length=15),
        ),
    ]
