# Generated by Django 4.1.3 on 2022-12-27 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0016_members_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.teacher'),
        ),
    ]