from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


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
