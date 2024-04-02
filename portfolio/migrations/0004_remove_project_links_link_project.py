# Generated by Django 5.0.3 on 2024-03-31 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0003_remove_technology_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="links",
        ),
        migrations.AddField(
            model_name="link",
            name="project",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="links",
                to="portfolio.project",
            ),
        ),
    ]