import factory
from factory.django import DjangoModelFactory

from app.models import Provider


class ProviderFactory(DjangoModelFactory):
    name = factory.Sequence('Provider #{} name'.format)
    email = factory.Sequence('provider{}@email.com'.format)
    currency = Provider.USD_CURRENCY
    language = Provider.ENGLISH_LANGUAGE
    phone_number = factory.Sequence('Provider #{} phone_number'.format)

    class Meta:
        model = Provider
