# Generated by Django 2.1.5 on 2019-07-29 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0004_auto_20190730_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]
