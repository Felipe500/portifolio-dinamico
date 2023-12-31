# Generated by Django 4.2.6 on 2023-12-06 14:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app_projects", "0001_initial"),
        ("app_website", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SoftSkill",
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
                ("name", models.CharField(max_length=200)),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Descrição"
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        default=1,
                        help_text="Número da ordem de exibição.",
                        verbose_name="Ordenação",
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
                "verbose_name": "Soft Skill",
                "verbose_name_plural": "Soft Skills",
            },
        ),
        migrations.CreateModel(
            name="HardSkill",
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
                ("name", models.CharField(max_length=200)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("solf_skill", "Solf Skill"),
                            ("hard_skill", "Hard Skill"),
                        ],
                        default="hard_skill",
                        verbose_name="Tipo",
                    ),
                ),
                (
                    "time_experience",
                    models.CharField(
                        choices=[
                            ("_0_year_0_month", "INICIANDO ESTUDOS"),
                            ("_0_year_6_month", "6 MESES"),
                            ("_1_year_0_month", "1 ANO"),
                            ("_1_year_6_month", "1 ANO E 6 MESES"),
                            ("_2_year_0_month", "2 ANO"),
                            ("_2_year_6_month", "2 ANO E 6 MESES"),
                            ("_3_year_0_month", "3 ANO"),
                            ("_3_year_6_month", "3 ANO E 6 MESES"),
                            ("_4_year_0_month", "4 ANO"),
                            ("_5_year_0_month", "5 ANO"),
                            ("_6_year_0_month", "6 ANO"),
                            ("_7_year_0_month", "7 ANO"),
                            ("_8_year_0_month", "8 ANO"),
                            ("_9_year_0_month", "9 ANO"),
                            ("_10_year_0_month", "10 ANO OU MAIS"),
                        ],
                        default="_0_year_0_month",
                        verbose_name="Tipo de Projeto",
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        default=1,
                        help_text="Número da ordem de exibição.",
                        verbose_name="Ordenação",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app_projects.project",
                        verbose_name="Projeto",
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
                "verbose_name": "Hard Skill",
                "verbose_name_plural": "Hard Skills",
                "ordering": ["order"],
            },
        ),
    ]
