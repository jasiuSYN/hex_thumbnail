# Generated by Django 4.1.7 on 2023-02-28 21:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0006_alter_image_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="tier",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.tier"
            ),
        ),
        migrations.AlterField(
            model_name="thumbnailsize",
            name="size",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(10),
                    django.core.validators.MaxValueValidator(720),
                ]
            ),
        ),
    ]
