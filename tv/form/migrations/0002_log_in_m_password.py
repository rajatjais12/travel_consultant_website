# Generated by Django 2.1.5 on 2019-08-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log_in_m',
            name='password',
            field=models.CharField(default='', max_length=32),
        ),
    ]
