# Please do not edit this file!
# It lists all the application Settings, and their default values.
# If you want to override any of the listed options,
# you can do it in local_settings.py
debug = False
logging = 'error'
address = '0.0.0.0'
port = 8000
static_path = 'static'
static_url_prefix = '/static/'
template_path = 'views'
gzip = False

# If you need handle HTTPS traffic uncomment next two lines and edit it to
# contain the correct path for the files the certificate and private key
# NOTE: keyfile must not be encrypted!
# certfile = 'server.crt'
# keyfile = 'server.pem'

try:
    from local_settings import *
except ImportError:
    pass
