# Generated by Django 4.0 on 2021-12-21 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticateUser', '0004_user_maximum_capacity_alter_user_disk_space'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPaymentAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishable_key', models.TextField()),
                ('secret_key', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authenticateUser.user')),
            ],
        ),
    ]
