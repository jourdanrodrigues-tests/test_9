import factory
from factory.django import DjangoModelFactory

from app.models import Provider, ServiceArea


class ProviderFactory(DjangoModelFactory):
    name = factory.Sequence('Provider #{}'.format)
    email = factory.Sequence('provider{}@email.com'.format)
    currency = Provider.USD_CURRENCY
    language = Provider.ENGLISH_LANGUAGE
    phone_number = factory.Sequence('Provider #{} phone_number'.format)

    class Meta:
        model = Provider


class ServiceAreaFactory(DjangoModelFactory):
    name = factory.Sequence('Service area #{}'.format)
    price = factory.Sequence(lambda i: i * 3.86)
    points = factory.Sequence(lambda i: [
        [2 + i, 2 + i],
        [0 + i, 0 + i],
        [1 + i, 0 + i],
    ])
    provider = factory.SubFactory(ProviderFactory)

    class Meta:
        model = ServiceArea
