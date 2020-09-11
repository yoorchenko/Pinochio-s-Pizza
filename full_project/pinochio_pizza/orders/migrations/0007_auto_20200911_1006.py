# Generated by Django 3.1 on 2020-09-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderer_id',
        ),
        migrations.AddField(
            model_name='order',
            name='orderer',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(blank=True),
        ),
    ]
