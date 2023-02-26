from rest_framework import generics
from api.models import Image, Tier
from api.serializers import ImageSerializer, TierSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ImageViewListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(profile__user=self.request.user)


class TierCreateAPIView(generics.CreateAPIView):
    serializer_class = TierSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        print(self.request)
        return Tier.objects.get_or_create()
