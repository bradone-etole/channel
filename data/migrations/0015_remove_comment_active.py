# Generated by Django 4.0.3 on 2022-04-03 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_alter_comment_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
    ]
