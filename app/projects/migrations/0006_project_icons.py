# Generated by Django 4.2.6 on 2023-12-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_projects", "0005_alter_project_cover_alter_project_thumbnail"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="icons",
            field=models.JSONField(default={}),
        ),
    ]