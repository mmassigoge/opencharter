exec('from settings import *')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'opencharter',
        'USER': 'desarrollo',
        'PASSWORD': 'desarrollo',
        'HOST': 'localhost',
    }
}
