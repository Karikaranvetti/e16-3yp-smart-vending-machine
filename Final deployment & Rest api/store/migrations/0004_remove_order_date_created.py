# Generated by Django 3.1.5 on 2021-01-22 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_created',
        ),
    ]
