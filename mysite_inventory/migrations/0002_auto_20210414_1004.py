# Generated by Django 3.2 on 2021-04-14 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite_inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Desktops',
            new_name='Desktop',
        ),
        migrations.RenameModel(
            old_name='Laptops',
            new_name='Laptop',
        ),
        migrations.RenameModel(
            old_name='Mobiles',
            new_name='Mobile',
        ),
    ]