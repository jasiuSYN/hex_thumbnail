from api.models import Image, Profile, ThumbnailSize, Tier


def test_thumbnail_size(size1, size2):
    assert isinstance(size1, ThumbnailSize)
    assert isinstance(size2, ThumbnailSize)


def test_tier(tier_basic, tier_premium):
    assert tier_basic.name == "test_basic"
    assert tier_premium.name == "test_premium"

    assert isinstance(tier_basic, Tier)
    assert isinstance(tier_premium, Tier)


def test_user_profile(user_profile):
    assert user_profile.user.is_staff == False
    assert isinstance(user_profile, Profile)


def test_admin_profile(admin_profile):
    assert admin_profile.user.is_superuser == True
    assert isinstance(admin_profile, Profile)


def test_profile_user_get_thumbnail_sizes(user_profile):
    assert user_profile.get_thumbnail_sizes() == [200]


def test_profile_admin_get_thumbnail_sizes(admin_profile):
    assert admin_profile.get_thumbnail_sizes() == [200, 400]


def test_image(image):
    assert isinstance(image, Image)
