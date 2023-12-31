# Generated by Django 4.2.6 on 2023-12-06 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_skills", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hardskill",
            name="type",
            field=models.CharField(
                choices=[
                    ("front_end", "FRONT-END"),
                    ("back_end", "BACK-END"),
                    ("mobile", "MOBILE"),
                    ("desktop", "DESKTOP"),
                ],
                default="back_end",
                verbose_name="Tipo",
            ),
        ),
    ]
