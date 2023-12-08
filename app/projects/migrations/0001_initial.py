# Generated by Django 4.2.6 on 2023-12-06 14:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app_website", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    model_utils.fields.AutoCreatedField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="Criado em",
                    ),
                ),
                (
                    "updated_at",
                    model_utils.fields.AutoLastModifiedField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="Modificado em",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Nome do projeto",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Descrição"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("full_stack", "Full-Stack"),
                            ("front_end", "Front-end"),
                            ("back_end", "Back-end"),
                            ("mobile", "Mobile"),
                            ("desktop", "Desktop"),
                        ],
                        default="full_stack",
                        verbose_name="Tipo de Projeto",
                    ),
                ),
                (
                    "demo_link",
                    models.CharField(
                        blank=True,
                        max_length=2000,
                        null=True,
                        verbose_name="Link do projeto em produção:",
                    ),
                ),
                (
                    "source_link",
                    models.CharField(
                        blank=True,
                        max_length=2000,
                        null=True,
                        verbose_name="Link do repositório do projeto:",
                    ),
                ),
                (
                    "website",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app_website.website",
                        verbose_name="Website",
                    ),
                ),
            ],
            options={
                "verbose_name": "Projeto",
                "verbose_name_plural": "Projetos",
            },
        ),
    ]
