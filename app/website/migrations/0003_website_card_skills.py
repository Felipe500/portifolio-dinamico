# Generated by Django 4.2.6 on 2023-12-07 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_website", "0002_alter_website_birth_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="website",
            name="card_skills",
            field=models.JSONField(default=list, verbose_name="Card de Habilidades"),
        ),
    ]
