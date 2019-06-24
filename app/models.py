from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from matplotlib.path import Path

from app.abstractions import Point


class PointField(ArrayField):
    def __init__(self, **kwargs):
        kwargs['size'] = 2
        kwargs['base_field'] = models.FloatField()
        super().__init__(**kwargs)

    def to_python(self, value):
        x, y = super().to_python(value)
        return Point(x, y)


class User(AbstractUser):
    pass


class Provider(models.Model):
    ENGLISH_LANGUAGE = 'en_US'
    BRAZILIAN_PORTUGUESE_LANGUAGE = 'pt_BR'

    LANGUAGE_CHOICES = (
        (ENGLISH_LANGUAGE, _('English')),
        (BRAZILIAN_PORTUGUESE_LANGUAGE, _('Brazilian Portuguese')),
    )

    USD_CURRENCY = 'USD'
    BRL_CURRENCY = 'BRL'

    CURRENCY_CHOICES = (
        (USD_CURRENCY, _('Dollar')),
        (BRL_CURRENCY, 'Real'),
    )

    name = models.CharField(_('Name'), max_length=100)
    email = models.EmailField()
    language = models.CharField(_('Language'), max_length=5, choices=LANGUAGE_CHOICES)
    currency = models.CharField(_('Currency'), max_length=3, choices=CURRENCY_CHOICES)
    phone_number = models.CharField(_('Phone number'), max_length=40)


class ServiceArea(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    price = models.FloatField(_('Price'))
    points = ArrayField(PointField())
    provider = models.ForeignKey(Provider, related_name='service_areas', on_delete=models.CASCADE)

    def to_geo_json(self):
        return {
            'type': 'Feature',
            'properties': {
                'id': self.id,
                'name': self.name,
                'price': self.price,
            },
            'geometry': {
                'type': 'Polygon',
                'coordinates': [
                    list(point) for point in self.points
                ],
            },
        }

    def contains(self, point: Point) -> bool:
        return Path(self.points).contains_point(point)
