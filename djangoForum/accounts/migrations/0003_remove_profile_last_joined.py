# Generated by Django 4.0.3 on 2022-03-22 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_forumuser_date_joined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_joined',
        ),
    ]
