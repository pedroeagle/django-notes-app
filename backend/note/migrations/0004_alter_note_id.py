# Generated by Django 3.2.6 on 2021-09-01 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_rename_user_id_note_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
