# Generated by Django 3.1 on 2020-09-01 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Extra_Subs',
            new_name='Extra_Sub',
        ),
        migrations.RenameModel(
            old_name='Subs',
            new_name='Sub',
        ),
        migrations.RenameModel(
            old_name='Toppings',
            new_name='Topping',
        ),
    ]
