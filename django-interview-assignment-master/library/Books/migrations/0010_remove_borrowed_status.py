# Generated by Django 4.0.6 on 2022-07-16 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0009_remove_borrowed_borrowed_till'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowed',
            name='status',
        ),
    ]
