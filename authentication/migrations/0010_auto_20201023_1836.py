# Generated by Django 3.1.2 on 2020-10-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_auto_20201023_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profession_type',
        ),
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.CharField(max_length=39, null=True),
        ),
    ]
