# Generated by Django 5.0.3 on 2024-04-24 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0006_alter_link_icon_alter_technology_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="link",
            name="icon",
            field=models.ImageField(blank=True, upload_to="icons/"),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(blank=True, upload_to="portfolio/projects/"),
        ),
        migrations.AlterField(
            model_name="technology",
            name="icon",
            field=models.ImageField(blank=True, upload_to="icons/"),
        ),
    ]
