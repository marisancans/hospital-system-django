# Generated by Django 2.2 on 2019-04-04 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190404_1022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='date_crated',
            new_name='date_created',
        ),
    ]
