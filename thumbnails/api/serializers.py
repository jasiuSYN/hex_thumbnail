from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers

from api.models import Image, Profile, ThumbnailSize, Tier


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


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

    def create(self, validated_data):
        thumbnail_sizes_data = validated_data.pop("thumbnail_size")
        thumbnail_sizes = []

        for thumbnail_size in thumbnail_sizes_data:
            size, _ = ThumbnailSize.objects.get_or_create(**thumbnail_size)
            thumbnail_sizes.append(size)

        with transaction.atomic():
            tier = Tier.objects.create(**validated_data)
            tier.thumbnail_size.add(*thumbnail_sizes)

        return tier


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tier = TierSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["user", "tier"]


class ImageSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Image
        fields = ["profile", "image"]
