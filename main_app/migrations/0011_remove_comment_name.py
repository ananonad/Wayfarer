# Generated by Django 4.0.2 on 2022-02-16 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]