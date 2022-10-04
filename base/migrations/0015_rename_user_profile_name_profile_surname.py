# Generated by Django 4.0.5 on 2022-08-06 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='surname',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
