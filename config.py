from os import environ

#TG Credentials
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

#Website Credentials
API_KEY = environ.get('API_KEY', '5d6505709fb29c5d45cd44c9fe75ba6c913252b8')
API_URL = environ.get('API_URL', 'https://viplinkshortx.in/api')
WEB_NAME = environ.get('WEB_NAME', 'VipLinkShortx')

#Optional
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', 'https://t.me/pandaztalks')
UPDATES_CHANNEL = environ.get('UPDATES_CHANNEL', 'https://t.me/pandaznetwork')
