# Generated by Django 5.0 on 2023-12-30 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_fname_watchmen_f_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchmen',
            old_name='f_name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='watchmen',
            old_name='l_name',
            new_name='lname',
        ),
        migrations.RenameField(
            model_name='watchmen',
            old_name='w_mobile',
            new_name='mobile',
        ),
    ]