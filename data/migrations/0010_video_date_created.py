# Generated by Django 4.0.3 on 2022-04-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_user_email_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
