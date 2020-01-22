# -*- coding: utf-8 -*-
import factory

import random
from django.conf import settings
from TWLight.resources.models import Partner, Stream, Video, Suggestion


class PartnerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Partner
        strategy = factory.CREATE_STRATEGY

    company_name = factory.Faker(
        "company", locale=random.choice(settings.FAKER_LOCALES)
    )
    terms_of_use = factory.Faker("uri", locale=random.choice(settings.FAKER_LOCALES))
    status = Partner.AVAILABLE  # not the default, but usually wanted in tests
    authorization_method = Partner.EMAIL

    # PROXY partners need requested_access_duration to be True, so we ensure
    # that field is set even if a test doesn't set it explicitly.
    @factory.lazy_attribute
    def requested_access_duration(self):
        if self.authorization_method == Partner.PROXY:
            return True
        else:
            return False


class StreamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Stream
        strategy = factory.CREATE_STRATEGY

    partner = factory.SubFactory(PartnerFactory)
    name = factory.Faker("bs", locale=random.choice(settings.FAKER_LOCALES))


class SuggestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Suggestion
        strategy = factory.CREATE_STRATEGY

    suggested_company_name = factory.Faker(
        "company", locale=random.choice(settings.FAKER_LOCALES)
    )
    company_url = factory.Faker("url", locale=random.choice(settings.FAKER_LOCALES))


class VideoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Video
        strategy = factory.CREATE_STRATEGY

    partner = factory.SubFactory(PartnerFactory)
