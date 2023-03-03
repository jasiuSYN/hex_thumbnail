from django.urls import path

from api.views import (ImageListAPIView, ImageUploadAPIView,
                       ProfileDetialsAPIView, TierCreateAPIView)

urlpatterns = [
    path("api/profile/detail", ProfileDetialsAPIView.as_view(), name="profile_detail"),
    path("api/image/list", ImageListAPIView.as_view(), name="image_list"),
    path("api/image/upload", ImageUploadAPIView.as_view(), name="image_upload"),
    path("api/tier/create", TierCreateAPIView.as_view(), name="tier_create"),
]
