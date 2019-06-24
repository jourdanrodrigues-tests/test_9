import os

from core.helpers import DotEnvReader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DotEnvReader(os.path.join(BASE_DIR, '.env')).read()

SECRET_KEY = os.getenv('SECRET_KEY')

PRODUCTION = bool(int(os.getenv('PRODUCTION', 0)))
DEBUG = bool(int(os.getenv('DEBUG', not PRODUCTION)))

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '' if PRODUCTION else '*').split(',')
