# Generated by Django 3.1.5 on 2021-01-31 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_product_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='place',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
