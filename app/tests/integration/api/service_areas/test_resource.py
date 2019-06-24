from rest_framework import status
from rest_framework.test import APITestCase

from app.factories import ServiceAreaFactory, ProviderFactory
from app.models import ServiceArea


class TestGet(APITestCase):
    def test_that_it_returns_200_status_code(self):
        response = self.client.get('/api/service_areas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_that_it_returns_correct_data(self):
        service_area = ServiceAreaFactory()

        response = self.client.get('/api/service_areas/')

        self.assertDictEqual(response.data[0], {
            'id': service_area.id,
            'name': service_area.name,
            'price': service_area.price,
            'provider': service_area.provider_id,
        })

    def test_that_it_returns_correct_amount_of_service_areas(self):
        ServiceAreaFactory.create_batch(13)

        response = self.client.get('/api/service_areas/')

        self.assertEqual(len(response.data), 13)


class TestGetOne(APITestCase):
    def test_when_service_area_does_not_exist_then_returns_404_status_code(self):
        response = self.client.get('/api/service_areas/0/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_that_it_returns_200_status_code(self):
        service_area = ServiceAreaFactory()

        response = self.client.get('/api/service_areas/{}/'.format(service_area.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_that_it_returns_correct_data(self):
        service_area = ServiceAreaFactory()

        response = self.client.get('/api/service_areas/{}/'.format(service_area.id))

        self.assertDictEqual(response.data, {
            'id': service_area.id,
            'name': service_area.name,
            'price': service_area.price,
            'provider': service_area.provider_id,
        })


class TestPost(APITestCase):

    def setUp(self) -> None:
        self.post_data = {
            'name': 'Some name',
            'price': 3.9,
            'points': [
                [1, 2],
                [2, 3],
                [0, 4],
            ],
            'provider': ProviderFactory().id,
        }

    def test_when_data_is_correct_then_returns_correct_data(self):
        response = self.client.post('/api/service_areas/', self.post_data, format='json')

        data = response.data
        expected_data = {'id': data.get('id'), **self.post_data.copy()}
        del expected_data['points']

        self.assertEqual(data, expected_data)

    def test_when_data_is_correct_then_creates_the_service_area(self):
        response = self.client.post('/api/service_areas/', self.post_data, format='json')

        service_area_exists = ServiceArea.objects.filter(id=response.data.get('id'), **self.post_data.copy()).exists()
        self.assertTrue(service_area_exists)

    def test_when_data_is_correct_then_returns_201_status_code(self):
        response = self.client.post('/api/service_areas/', self.post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestPatch(APITestCase):
    def test_when_data_is_correct_then_returns_correct_data(self):
        service_area = ServiceAreaFactory(name='Weird name')
        patch_data = {'name': 'Cool name'}

        response = self.client.patch('/api/service_areas/{}/'.format(service_area.id), patch_data, format='json')

        data = response.data
        self.assertEqual(data, {
            'id': service_area.id,
            'name': patch_data['name'],
            'price': service_area.price,
            'provider': service_area.provider_id,
        })

    def test_when_data_is_correct_then_returns_200_status_code(self):
        service_area = ServiceAreaFactory(name='Weird name')
        patch_data = {'name': 'Cool name'}

        response = self.client.patch('/api/service_areas/{}/'.format(service_area.id), patch_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_when_service_area_does_not_exist_then_returns_404_status_code(self):
        response = self.client.patch('/api/service_areas/0/', {})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_when_data_is_correct_then_updates_the_service_area(self):
        service_area = ServiceAreaFactory(name='Weird name')
        patch_data = {'name': 'Cool name'}

        self.client.patch('/api/service_areas/{}/'.format(service_area.id), patch_data, format='json')

        service_area_exists = ServiceArea.objects.filter(id=service_area.id, name=patch_data['name']).exists()
        self.assertTrue(service_area_exists)


class TestDelete(APITestCase):
    def test_that_it_deletes_the_service_area(self):
        service_area_id = ServiceAreaFactory().id

        self.client.delete('/api/service_areas/{}/'.format(service_area_id))

        self.assertFalse(ServiceArea.objects.filter(id=service_area_id).exists())

    def test_that_it_returns_204_status_code(self):
        service_area_id = ServiceAreaFactory().id

        response = self.client.delete('/api/service_areas/{}/'.format(service_area_id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_when_service_area_does_not_exist_then_returns_404_status_code(self):
        response = self.client.delete('/api/service_areas/0/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
