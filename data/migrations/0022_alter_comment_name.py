# Generated by Django 4.0.3 on 2022-04-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0021_alter_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
