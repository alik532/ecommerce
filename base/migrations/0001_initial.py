# Generated by Django 4.0.5 on 2022-08-04 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSegregation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.TextField(blank=True, max_length=200)),
                ('reputation', models.IntegerField(blank=True)),
            ],
        ),
    ]
