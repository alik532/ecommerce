# Generated by Django 4.0.5 on 2022-08-05 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_shift_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='user',
            field=models.ManyToManyField(blank=True, to='base.usersegregation'),
        ),
    ]
