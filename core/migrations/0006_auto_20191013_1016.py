# Generated by Django 2.2 on 2019-10-13 10:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191013_0548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='code',
        ),
        migrations.AddField(
            model_name='coupon',
            name='OD_Axis',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(58)]),
        ),
        migrations.AddField(
            model_name='coupon',
            name='OD_cylinder',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='coupon',
            name='OD_sphere',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='coupon',
            name='OS_Axis',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(58)]),
        ),
        migrations.AddField(
            model_name='coupon',
            name='OS_cylinder',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='coupon',
            name='OS_sphere',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='coupon',
            name='correction',
            field=models.CharField(choices=[('DV', 'Distant Vision'), ('CV', 'Close Vision')], default='DV', max_length=2),
        ),
    ]