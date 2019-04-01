# Generated by Django 2.1.7 on 2019-03-31 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_medhistory_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='patient',
        ),
        migrations.AddField(
            model_name='room',
            name='patient',
            field=models.ManyToManyField(to='app.Patient'),
        ),
    ]