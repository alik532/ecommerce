# Generated by Django 4.0.5 on 2022-08-04 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_usersegregation_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersegregation',
            old_name='User',
            new_name='user',
        ),
    ]
