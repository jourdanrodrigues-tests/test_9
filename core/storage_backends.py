import os

from uuid import uuid4

# noinspection PyPackageRequirements
from storages.backends.s3boto3 import S3Boto3Storage


# noinspection PyAbstractClass
class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

    def get_available_name(self, name, max_length=None):
        dir_name, file_name = os.path.split(name)
        _, file_ext = os.path.splitext(file_name)

        new_file_name = str(uuid4()).replace('-', '') + file_ext

        return os.path.join(dir_name, new_file_name)


# noinspection PyAbstractClass
class StaticStorage(S3Boto3Storage):
    location = 'static'
    file_overwrite = True
