from rest_framework import status
from rest_framework.test import APITestCase

from app.factories import ProviderFactory
from app.models import Provider


class TestGet(APITestCase):
    def test_that_it_returns_200_status_code(self):
        response = self.client.get('/api/providers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_that_it_returns_correct_data(self):
        provider = ProviderFactory()

        response = self.client.get('/api/providers/')

        self.assertDictEqual(response.data[0], {
            'id': provider.id,
            'name': provider.name,
            'email': provider.email,
            'language': provider.language,
            'currency': provider.currency,
            'phone_number': provider.phone_number,
        })

    def test_that_it_returns_correct_amount_of_providers(self):
        ProviderFactory.create_batch(13)

        response = self.client.get('/api/providers/')

        self.assertEqual(len(response.data), 13)


class TestGetOne(APITestCase):
    def test_when_provider_does_not_exist_then_returns_404_status_code(self):
        response = self.client.get('/api/providers/0/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_that_it_returns_200_status_code(self):
        provider_id = ProviderFactory().id

        response = self.client.get('/api/providers/{}/'.format(provider_id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_that_it_returns_correct_data(self):
        provider = ProviderFactory()

        response = self.client.get('/api/providers/{}/'.format(provider.id))

        self.assertDictEqual(response.data, {
            'id': provider.id,
            'name': provider.name,
            'email': provider.email,
            'language': provider.language,
            'currency': provider.currency,
            'phone_number': provider.phone_number,
        })


class TestPost(APITestCase):
    post_data = {
        'name': 'Some name',
        'email': 'random@email.com',
        'language': Provider.BRAZILIAN_PORTUGUESE_LANGUAGE,
        'currency': Provider.USD_CURRENCY,
        'phone_number': '+55 (85) 9 9999-9999',
    }

    def test_when_data_is_correct_then_returns_correct_data(self):
        response = self.client.post('/api/providers/', self.post_data)

        data = response.data
        expected_data = {'id': data.get('id'), **self.post_data.copy()}
        self.assertEqual(data, expected_data)

    def test_when_data_is_correct_then_creates_the_provider(self):
        response = self.client.post('/api/providers/', self.post_data)

        provider_exists = Provider.objects.filter(id=response.data.get('id'), **self.post_data.copy()).exists()
        self.assertTrue(provider_exists)

    def test_when_data_is_correct_then_returns_201_status_code(self):
        response = self.client.post('/api/providers/', self.post_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestPatch(APITestCase):
    def test_when_data_is_correct_then_returns_correct_data(self):
        provider = ProviderFactory(name='Weird name')
        patch_data = {'name': 'Cool name'}

        response = self.client.patch('/api/providers/{}/'.format(provider.id), patch_data)

        data = response.data
        self.assertEqual(data, {
            'id': provider.id,
            'name': patch_data['name'],
            'email': provider.email,
            'language': provider.language,
            'currency': provider.currency,
            'phone_number': provider.phone_number,
        })

    def test_when_data_is_correct_then_returns_200_status_code(self):
        provider = ProviderFactory(name='Weird name')
        patch_data = {'name': 'Cool name'}

        response = self.client.patch('/api/providers/{}/'.format(provider.id), patch_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_when_provider_does_not_exist_then_returns_404_status_code(self):
        response = self.client.patch('/api/providers/0/', {})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_when_data_is_correct_then_updates_the_provider(self):
        provider = ProviderFactory(name='Weird name')
        patch_data = {'name': 'Cool name'}

        self.client.patch('/api/providers/{}/'.format(provider.id), patch_data)

        provider_exists = Provider.objects.filter(id=provider.id, name=patch_data['name']).exists()
        self.assertTrue(provider_exists)


class TestDelete(APITestCase):
    def test_that_it_deletes_the_provider(self):
        provider_id = ProviderFactory().id

        self.client.delete('/api/providers/{}/'.format(provider_id))

        self.assertFalse(Provider.objects.filter(id=provider_id).exists())

    def test_that_it_returns_204_status_code(self):
        provider_id = ProviderFactory().id

        response = self.client.delete('/api/providers/{}/'.format(provider_id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_when_provider_does_not_exist_then_returns_404_status_code(self):
        response = self.client.delete('/api/providers/0/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
