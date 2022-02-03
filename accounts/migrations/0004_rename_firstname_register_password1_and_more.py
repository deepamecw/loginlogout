# Generated by Django 4.0 on 2022-01-26 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_register_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='firstname',
            new_name='password1',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='lastname',
            new_name='password2',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='place',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='register',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='register',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='register',
            name='state',
        ),
        migrations.AlterModelTable(
            name='register',
            table='reg_details',
        ),
    ]