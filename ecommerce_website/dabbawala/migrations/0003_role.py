# Generated by Django 4.1.7 on 2023-04-29 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dabbawala', '0002_alter_user_managers_user_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.CharField(max_length=25, null=True)),
            ],
        ),
    ]
