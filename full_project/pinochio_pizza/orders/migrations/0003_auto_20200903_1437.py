# Generated by Django 3.1 on 2020-09-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(blank=True, to='orders.Item'),
        ),
    ]