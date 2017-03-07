import os

config = {
    'port': os.environ.get('PORT') or 5000,
    'recast': {
        'token': os.environ.get('RECAST_TOKEN') or '',
        'language': os.environ.get('RECAST_LANGUAGE') or ''
    }
}
