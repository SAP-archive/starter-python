import os

config = {
    'port': os.environ.get('PORT', 5000),
    'recast': {
        'token': os.environ.get('RECAST_TOKEN', ''),
        'language': os.environ.get('RECAST_LANGUAGE', '')
    }
}
