# Generated by Django 4.0.5 on 2022-08-05 03:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0006_remove_shift_user_shift_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]