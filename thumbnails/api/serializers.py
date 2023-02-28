from django.db import transaction
from rest_framework import serializers
from easy_thumbnails.files import get_thumbnailer

from api.models import Image, ThumbnailSize, Tier, Profile


class ThumbnailSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThumbnailSize
        fields = ["size"]


class TierSerializer(serializers.ModelSerializer):
    thumbnail_size = ThumbnailSizeSerializer(many=True)

    class Meta:
        model = Tier
        fields = [
            "name",
            "thumbnail_size",
            "allow_original_file_link",
            "allow_expiring_links",
        ]

    @transaction.atomic
    def create(self, validated_data):
        thumbnail_sizes_data = validated_data.pop("thumbnail_size")
        thumbnail_sizes_instaces = []

        for thumbnail_size in thumbnail_sizes_data:
            size_instance, _ = ThumbnailSize.objects.get_or_create(**thumbnail_size)
            thumbnail_sizes_instaces.append(size_instance)

        tier = Tier.objects.create(**validated_data)
        tier.thumbnail_size.add(*thumbnail_sizes_instaces)
        tier.save()

        return tier


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["profile", "image"]


class ThumbnailSerializer(serializers.ModelSerializer):
    thumbnails = serializers.SerializerMethodField()
    allow_expiring_links = serializers.SerializerMethodField()

    def create(self, validated_data):
        user = self.context["request"].user
        profile = user.profile
        validated_data["profile"] = profile

        return super().create(validated_data)

    def get_thumbnails(self, obj):
        user_tier_sizes = obj.profile.get_thumbnail_sizes()
        thumbnail_urls = {}
        for size in user_tier_sizes:
            thumbnail_options = {"size": (size, 0), "crop": True}
            thumbnail_url = (
                get_thumbnailer(obj.image).get_thumbnail(thumbnail_options).url
            )
            thumbnail_urls[f"thumbnail_{size}"] = thumbnail_url

        return thumbnail_urls

    def get_allow_expiring_links(self, obj):
        return obj.profile.tier.allow_expiring_links

    class Meta:
        model = Image
        fields = ["image", "thumbnails", "allow_expiring_links"]
