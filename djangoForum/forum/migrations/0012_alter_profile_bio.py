# Generated by Django 4.0.3 on 2022-04-09 11:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_alter_forumpost_content_alter_forumthread_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
