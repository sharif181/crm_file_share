# Generated by Django 4.0 on 2021-12-13 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_management', '0006_file_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='expire_days',
            field=models.IntegerField(default=7),
        ),
    ]