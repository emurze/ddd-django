

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://cache:6380',
        'OPTIONS': {
            'db': 1
        },
    }
}
