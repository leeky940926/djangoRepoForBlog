# Generated by Django 4.0.3 on 2022-03-05 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='customer',
            name='indexes_cus_last_na_cc0e9b_idx',
        ),
    ]
