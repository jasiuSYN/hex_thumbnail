import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from api.tests.factories import (ImageFactory, ProfileFactory,
                                 ThumbnailSizeFactory, TierFactory)

register(ThumbnailSizeFactory)
register(TierFactory)
register(ProfileFactory)
register(ImageFactory)


@pytest.fixture
def size1(db, thumbnail_size_factory):
    size1 = thumbnail_size_factory.create()
    return size1


@pytest.fixture
def size2(db, thumbnail_size_factory):
    size2 = thumbnail_size_factory.create(size=400)
    return size2


@pytest.fixture
def tier_basic(db, tier_factory, size1):
    tier_basic = tier_factory.create(name="test_basic")
    tier_basic.thumbnail_size.add(size1)
    return tier_basic


@pytest.fixture
def tier_premium(db, tier_factory, size1, size2):
    tier_premium = tier_factory.create(name="test_premium")
    tier_premium.thumbnail_size.add(size1, size2)
    return tier_premium


@pytest.fixture
def user_profile(db, profile_factory, tier_basic):
    new_user = profile_factory.create(tier=tier_basic)
    return new_user


@pytest.fixture
def admin_profile(db, profile_factory, tier_premium):
    new_admin = profile_factory.create(
        tier=tier_premium, user__is_staff=True, user__is_superuser=True
    )
    return new_admin


@pytest.fixture
def image(db, image_factory):
    image = image_factory.create()
    return image
