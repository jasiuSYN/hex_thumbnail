from django.urls import path

from .views import ImageListAPIView, ImageUploadAPIView, TierCreateAPIView

urlpatterns = [
    path("api/image/list", ImageListAPIView.as_view(), name="image_list"),
    path("api/image/upload", ImageUploadAPIView.as_view(), name="image_upload"),
    path("api/tier/create", TierCreateAPIView.as_view(), name="tier_create"),
]
