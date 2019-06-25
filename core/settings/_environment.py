import os

from core.helpers import DotEnvReader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DotEnvReader(os.path.join(BASE_DIR, '.env')).read()

SECRET_KEY = os.getenv('SECRET_KEY')

PRODUCTION = bool(int(os.getenv('PRODUCTION', 0)))
DEBUG = bool(int(os.getenv('DEBUG', not PRODUCTION)))

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '' if PRODUCTION else '*').split(',')

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
