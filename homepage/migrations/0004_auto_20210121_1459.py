# Generated by Django 3.1.5 on 2021-01-21 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_modul_banner_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modul',
            name='banner_img',
            field=models.FileField(default=None, upload_to='images/modul/'),
        ),
    ]