# Generated by Django 4.0.5 on 2022-08-12 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0035_alter_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
