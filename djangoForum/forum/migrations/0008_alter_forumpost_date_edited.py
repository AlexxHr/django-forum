# Generated by Django 4.0.3 on 2022-04-02 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_forumpost_date_edited_forumpost_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='date_edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]