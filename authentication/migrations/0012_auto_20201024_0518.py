# Generated by Django 3.1.2 on 2020-10-24 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_user_password2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password2',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
