# Generated by Django 4.1.7 on 2023-02-26 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="user",
        ),
        migrations.AddField(
            model_name="image",
            name="profile",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="api.profile"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="tier",
            name="thumbnail_size",
            field=models.ManyToManyField(
                related_name="thumbnail_sizes", to="api.thumbnailsize"
            ),
        ),
    ]
