# Generated by Django 2.2 on 2019-08-01 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_book_desc_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='desc_url',
            field=models.CharField(default='add a description url', max_length=200),
        ),
    ]
