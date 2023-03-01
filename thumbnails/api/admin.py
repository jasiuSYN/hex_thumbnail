from django.contrib import admin

from api.models import Image, Profile, ThumbnailSize, Tier

# Register your models here.

admin.site.register(ThumbnailSize)
admin.site.register(Tier)
admin.site.register(Profile)
admin.site.register(Image)
