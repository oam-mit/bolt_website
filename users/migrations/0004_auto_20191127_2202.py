# Generated by Django 2.2.7 on 2019-11-27 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191127_2200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='code',
            new_name='country',
        ),
    ]