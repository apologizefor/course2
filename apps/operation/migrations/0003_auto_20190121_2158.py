# Generated by Django 2.1.5 on 2019-01-21 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20190121_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermessage',
            old_name='has_red',
            new_name='has_read',
        ),
    ]