# Generated by Django 4.2.6 on 2023-12-07 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_website", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="website",
            name="birth_date",
            field=models.DateField(
                default=datetime.date(2023, 12, 7), verbose_name="Data de Nascimento"
            ),
        ),
    ]
