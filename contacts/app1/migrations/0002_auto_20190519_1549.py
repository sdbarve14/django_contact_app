# Generated by Django 2.2.1 on 2019-05-19 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='data_added',
            new_name='date_added',
        ),
    ]
