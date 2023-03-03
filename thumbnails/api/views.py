from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from api.models import Image, Profile
from api.serializers import (ImageSerializer, ProfileSerializer,
                             ThumbnailSerializer, TierSerializer)


class ImageListAPIView(generics.ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(profile__user=self.request.user)


class ProfileDetialsAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user_id=self.request.user.id)


class ImageUploadAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ThumbnailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        profile = request.user.profile
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if profile.tier.allow_original_file_link == False:
            return Response(
                serializer.data.get("thumbnails"), status=status.HTTP_201_CREATED
            )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TierCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TierSerializer
