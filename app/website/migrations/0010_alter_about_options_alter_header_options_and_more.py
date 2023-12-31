# Generated by Django 4.2.6 on 2023-12-17 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "app_website",
            "0009_remove_website_address_remove_website_birth_date_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="about",
            options={
                "verbose_name": "Sobre Website",
                "verbose_name_plural": "Sobre Website",
            },
        ),
        migrations.AlterModelOptions(
            name="header",
            options={
                "verbose_name": "Cabeçalho Website",
                "verbose_name_plural": "Cabeçalho Website",
            },
        ),
        migrations.RenameField(
            model_name="header",
            old_name="header_photo",
            new_name="photo",
        ),
    ]
