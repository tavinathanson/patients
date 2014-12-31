import os

def handle_false(value):
    """Ensure that false in config isn't interpreted as True."""
    if value and value.lower() == 'false':
        value = False
    return value

USE_RELOADER = handle_false(os.environ.get('USE_RELOADER', False))
PORT = int(os.environ.get('PORT', 5000))
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']

