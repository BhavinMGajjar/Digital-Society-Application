# Generated by Django 5.0 on 2023-12-30 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_watchmen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchmen',
            old_name='fname',
            new_name='f_name',
        ),
        migrations.RenameField(
            model_name='watchmen',
            old_name='lname',
            new_name='l_name',
        ),
        migrations.RenameField(
            model_name='watchmen',
            old_name='mobile',
            new_name='w_mobile',
        ),
    ]
