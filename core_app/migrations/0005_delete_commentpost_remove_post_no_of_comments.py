# Generated by Django 4.0.5 on 2022-12-20 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0004_post_no_of_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentPost',
        ),
        migrations.RemoveField(
            model_name='post',
            name='no_of_comments',
        ),
    ]
