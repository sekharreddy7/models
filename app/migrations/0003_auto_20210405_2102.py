# Generated by Django 3.1.7 on 2021-04-05 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210403_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='access_records',
            old_name='pub_date',
            new_name='date',
        ),
    ]
