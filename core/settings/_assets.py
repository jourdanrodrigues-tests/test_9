import os

from core.settings._environment import BASE_DIR, PRODUCTION, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME

AWS_S3_HOST = 's3.amazonaws.com'
S3_USE_SIGV4 = True
AWS_BUCKET_ACL = None
AWS_DEFAULT_ACL = None


def build_s3_url(path):
    return '//{}.{}/{}/{}/'.format(AWS_S3_REGION_NAME, AWS_S3_HOST, AWS_STORAGE_BUCKET_NAME, path)


if PRODUCTION:
    MEDIA_URL = build_s3_url('media')
    STATIC_URL = build_s3_url('static')

    DEFAULT_FILE_STORAGE = 'core.storage_backends.MediaStorage'
    STATICFILES_STORAGE = 'core.storage_backends.StaticStorage'
else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'assets', 'media')

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'assets', 'static')
