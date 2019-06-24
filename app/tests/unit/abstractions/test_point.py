from django.test import SimpleTestCase

from app.abstractions import Point


class TestInstance(SimpleTestCase):
    def test_that_it_can_be_parsed_into_a_list(self):
        self.assertListEqual(list(Point(1, 2)), [1, 2])
