# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("hordak", "0019_statementimport_source")]

    operations = [
        migrations.AddField(
            model_name="statementimport",
            name="extra",
            field=models.JSONField(
                default={},
                help_text="Any extra data relating to the import, probably specific to the data source.",
            ),
        ),
        migrations.AddField(
            model_name="statementline",
            name="source_data",
            field=models.JSONField(
                default={}, help_text="Original data received from the data source."
            ),
        ),
        migrations.AddField(
            model_name="statementline",
            name="type",
            field=models.CharField(default="", max_length=50),
        ),
    ]
