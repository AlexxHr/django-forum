# Generated by Django 4.0.3 on 2022-04-07 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_forumpost_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forumpost',
            options={'ordering': ['date_posted']},
        ),
        migrations.AddField(
            model_name='forumpost',
            name='is_reply',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='forum.forumpost'),
        ),
    ]
