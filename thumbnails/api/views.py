from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from api.models import Image
from api.serializers import (ImageSerializer, ThumbnailSerializer,
                             TierSerializer)


class ImageListAPIView(generics.ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(profile__user=self.request.user)


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
