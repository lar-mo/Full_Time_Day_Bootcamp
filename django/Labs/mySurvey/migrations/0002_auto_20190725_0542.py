# Generated by Django 2.2 on 2019-07-25 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mySurvey', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='pchoice_text',
            new_name='choice_text',
        ),
    ]
