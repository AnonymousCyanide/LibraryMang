# Generated by Django 4.0.6 on 2022-07-16 19:21

import Books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0005_borrowed_borrowed_till_borrowed_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed',
            name='borrowed_till',
            field=models.DateTimeField(),
        ),
    ]