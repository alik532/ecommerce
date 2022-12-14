# Generated by Django 4.0.5 on 2022-08-06 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
