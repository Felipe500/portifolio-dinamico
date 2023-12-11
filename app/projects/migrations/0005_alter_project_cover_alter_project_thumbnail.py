# Generated by Django 4.2.6 on 2023-12-08 20:04

import app.common.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_projects", "0004_project_cover_project_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="cover",
            field=app.common.fields.ImageField(
                blank=True,
                null=True,
                upload_to="projects/cover/%Y/%m/%d/",
                verbose_name="Capa",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="thumbnail",
            field=app.common.fields.ImageField(
                blank=True,
                null=True,
                upload_to="projects/thumbnails/",
                verbose_name="Miniatura da Capa",
            ),
        ),
    ]