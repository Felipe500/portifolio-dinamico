# Generated by Django 4.2.6 on 2023-12-16 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_website_data", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="About",
        ),
        migrations.DeleteModel(
            name="Header",
        ),
        migrations.DeleteModel(
            name="SocialMedia",
        ),
    ]