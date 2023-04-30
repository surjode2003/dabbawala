# Generated by Django 4.1.7 on 2023-04-29 17:03

import dabbawala.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dabbawala', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', dabbawala.manager.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
