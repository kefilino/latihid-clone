# Generated by Django 3.1.5 on 2021-01-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20210121_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='modul',
            name='uri',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
