# Generated by Django 4.2.6 on 2023-12-08 15:00

import app.common.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_projects", "0003_remove_project_skills_project_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="cover",
            field=app.common.fields.ImageField(
                blank=True, null=True, upload_to="projects/cover/%Y/%m/%d/"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="thumbnail",
            field=app.common.fields.ImageField(
                blank=True,
                null=True,
                upload_to="projects/thumbnails/",
                verbose_name="Miniatura foto",
            ),
        ),
    ]
