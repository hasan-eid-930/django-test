# Generated by Django 4.1.3 on 2022-12-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_alter_members_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]
