# Generated by Django 3.2.6 on 2021-09-01 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='user',
            new_name='user_id',
        ),
    ]