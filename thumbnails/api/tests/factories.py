import factory
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from factory.django import DjangoModelFactory
from faker import Faker

from api.models import Image, Profile, ThumbnailSize, Tier

faker = Faker()


@factory.django.mute_signals(post_save)
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    username = "test_username"

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)


class ThumbnailSizeFactory(DjangoModelFactory):
    class Meta:
        model = ThumbnailSize

    size = 200


class TierFactory(DjangoModelFactory):
    class Meta:
        model = Tier
        django_get_or_create = ("name",)

    name = "test_tier"
    allow_original_file_link = False
    allow_expiring_links = False

    @factory.post_generation
    def thumbnail_size(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for size in extracted:
                self.thumbnail_size.add(size)


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    tier = factory.SubFactory(TierFactory)


class ImageFactory(DjangoModelFactory):
    class Meta:
        model = Image

    profile = factory.SubFactory(ProfileFactory)
    image = factory.django.ImageField(
        width=720, height=720, color="green", format="PNG"
    )
