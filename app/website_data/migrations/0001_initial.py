# Generated by Django 4.2.6 on 2023-12-06 14:07

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app_website", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="About",
            fields=[],
            options={
                "verbose_name": "Sobre Mim",
                "verbose_name_plural": "Sobre Mim",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("app_website.website",),
        ),
        migrations.CreateModel(
            name="Header",
            fields=[],
            options={
                "verbose_name": "Cabeçalho da página",
                "verbose_name_plural": "Cabeçalhos das páginas",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("app_website.website",),
        ),
        migrations.CreateModel(
            name="SocialMedia",
            fields=[],
            options={
                "verbose_name": "Midia Social",
                "verbose_name_plural": "Midias Sociais",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("app_website.website",),
        ),
    ]
