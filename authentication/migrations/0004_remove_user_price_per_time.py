# Generated by Django 3.1.2 on 2020-10-22 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20201022_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='price_per_time',
        ),
    ]
