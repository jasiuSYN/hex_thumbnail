from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

# Create your models here.


class ThumbnailSize(models.Model):
    size = models.PositiveIntegerField()

    def __str__(self):
        return str(self.size)


class Tier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    thumbnail_size = models.ManyToManyField(
        ThumbnailSize, related_name="thumbnail_sizes"
    )
    allow_original_file_link = models.BooleanField(default=False)
    allow_expiring_links = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    tier = models.OneToOneField(Tier, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.tier}"


class Image(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(
        blank=True, upload_to="", validators=[FileExtensionValidator(["jpeg", "png"])]
    )
