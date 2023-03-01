import os

from django.contrib.auth import get_user_model
from django.core.validators import (FileExtensionValidator, MaxValueValidator,
                                    MinValueValidator)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


def get_user_directory_path(instance, filename):
    user_id = instance.profile.user_id
    return os.path.join("users", f"id_{str(user_id)}", filename)


class ThumbnailSize(models.Model):
    size = models.PositiveIntegerField(
        unique=True, validators=[MinValueValidator(10), MaxValueValidator(720)]
    )

    def __str__(self):
        return str(self.size)


class Tier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    thumbnail_size = models.ManyToManyField(ThumbnailSize)
    allow_original_file_link = models.BooleanField(default=False)
    allow_expiring_links = models.BooleanField(default=False)

    def __str__(self):
        return self.name


@receiver(post_save, sender=get_user_model())
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="profile"
    )
    tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user} {self.tier}" if self.tier else f"{self.user}"

    def get_thumbnail_sizes(self):
        sizes = self.tier.thumbnail_size.all()
        return [size.size for size in sizes]


class Image(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(
        blank=True,
        upload_to=get_user_directory_path,
        validators=[FileExtensionValidator(["jpeg", "png"])],
    )
