# Generated by Django 4.0.3 on 2022-03-24 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_remove_forumpost_category_forumpost_thread'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumthread',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, null=True),
        ),
    ]
