from django.urls import path
from .views import ImageViewListCreateAPIView, TierCreateAPIView

urlpatterns = [
    path("api/images/", ImageViewListCreateAPIView.as_view(), name="images_user"),
    path("api/tiers/", TierCreateAPIView.as_view(), name="tier_create"),
]
