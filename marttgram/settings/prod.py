
from django.conf import settings


SECRET_KEY = os.getenv('MARTT_SECRET_KEY')

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ALLOWED_HOSTS = ['3.84.116.226']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST' : os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
