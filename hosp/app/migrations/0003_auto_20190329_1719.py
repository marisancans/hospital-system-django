# Generated by Django 2.1.7 on 2019-03-29 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190329_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medhistory',
            name='sick_hist_id',
        ),
        migrations.AddField(
            model_name='person',
            name='sick_hist_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.SickHistory'),
        ),
    ]