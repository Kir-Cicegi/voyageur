# Generated by Django 3.2.4 on 2021-07-07 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210707_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airline',
            old_name='name',
            new_name='airline',
        ),
    ]