# Generated by Django 2.1.5 on 2019-11-03 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0013_auto_20190828_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_r',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='them_productf', to='package.Price_list'),
        ),
    ]