# Generated by Django 4.0.5 on 2022-08-12 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_rename_user_comment_author_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.TextField(blank=True),
        ),
    ]