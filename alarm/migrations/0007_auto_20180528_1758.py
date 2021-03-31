# Generated by Django 2.0 on 2018-05-28 15:58

import alarm.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0006_auto_20180520_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='tone',
            field=models.ForeignKey(default=alarm.models.default_ringtone, on_delete=django.db.models.deletion.SET_DEFAULT, to='storage.FileSong'),
        ),
    ]