from django.test import SimpleTestCase

from core.storage_backends import MediaStorage


class TestGetAvailableName(SimpleTestCase):
    def test_that_it_returns_uuid_file_name(self):
        file_name = 'fake/path/to/file.jpg'

        available_file_name = MediaStorage().get_available_name(file_name)

        self.assertRegex(available_file_name, r'fake/path/to/[a-z0-9]{8}([a-z0-9]{4}){3}[a-z0-9]{12}\.jpg')
