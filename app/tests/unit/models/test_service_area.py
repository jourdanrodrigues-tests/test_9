from django.test import SimpleTestCase

from app.abstractions import Point
from app.models import ServiceArea


class TestToGeoJson(SimpleTestCase):
    def test_that_it_returns_correct_data(self):
        service_area = ServiceArea(id=1, name='Cool name', price=150.82, points=[
            Point(-111.92, 33.53),
            Point(-111.96, 33.51),
            Point(-111.90, 33.50),
        ])

        self.assertDictEqual(service_area.to_geo_json(), {
            'type': 'Feature',
            'properties': {
                'id': service_area.id,
                'name': service_area.name,
                'price': service_area.price,
            },
            'geometry': {
                'type': 'Polygon',
                'coordinates': [
                    [-111.92, 33.53],
                    [-111.96, 33.51],
                    [-111.90, 33.50],
                ],
            },
        })


class TestContains(SimpleTestCase):
    def test_when_point_is_inside_the_service_area_then_returns_true(self):
        service_area = ServiceArea(points=[
            Point(-111.92, 33.53),
            Point(-111.96, 33.51),
            Point(-111.90, 33.50),
        ])
        self.assertTrue(service_area.contains(Point(-111.92, 33.52)))

    def test_when_point_is_not_inside_the_service_area_then_returns_false(self):
        service_area = ServiceArea(points=[
            Point(-111.92, 33.53),
            Point(-111.96, 33.51),
            Point(-111.90, 33.50),
        ])
        self.assertFalse(service_area.contains(Point(-111.92, 32.52)))
