# Generated by Django 4.1.3 on 2022-12-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_members_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='birthdate',
            field=models.DateField(auto_now=True),
        ),
    ]
