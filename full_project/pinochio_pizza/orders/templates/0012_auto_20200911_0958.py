# Generated by Django 3.1 on 2020-09-11 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200911_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='done',
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderer_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]
