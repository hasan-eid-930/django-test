# Generated by Django 4.1.3 on 2023-01-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0034_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='b',
            field=models.BooleanField(default=True),
        ),
    ]