# Generated by Django 4.0.7 on 2022-09-18 08:51

import django.contrib.postgres.fields
from django.db import migrations, models
import hordak.models.core


class Migration(migrations.Migration):
    dependencies = [
        ("hordak", "0030_alter_leg_amount_currency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="currencies",
            field=models.JSONField(
                verbose_name="currencies",
            ),
        ),
    ]
