# Generated by Django 5.0.3 on 2024-04-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0008_alter_link_icon_alter_project_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="demo",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="github",
            field=models.URLField(default="https://github.com/"),
            preserve_default=False,
        ),
    ]
