# Generated by Django 2.2 on 2019-08-01 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20190731_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image_url',
            field=models.CharField(default='https://lar-mo.com/images/lazy_placeholder.gif', max_length=200),
        ),
        migrations.AlterField(
            model_name='bookcheckout',
            name='checkin_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='bookcheckout',
            name='checkout_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]