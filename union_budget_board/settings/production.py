from .base import *
import json

with open(os.path.join(BASE_DIR, 'settings') + '/production.json', 'r') as f:
    config = json.load(f)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DEBUG = config['DEBUG']['STATUS']

SECRET_KEY = config['DEFAULT']['SECRET_KEY']

DATABASES = {
    'default': {
        'CONN_MAX_AGE': config['DATABASES']['CONN_MAX_AGE'],
        'ENGINE': config['DATABASES']['ENGINE'],
        'HOST': config['DATABASES']['HOST'],
        'NAME': config['DATABASES']['NAME'],
        'PASSWORD': config['DATABASES']['PASSWORD'],
        'PORT': config['DATABASES']['PORT'],
        'USER': config['DATABASES']['USER']
    }
}

ALLOWED_HOSTS = config["HOSTS"]["ALLOWED_HOSTS"]

#DjangoCMS Meta Settings as per: http://django-meta.readthedocs.io/en/latest/settings.html
META_SITE_PROTOCOL = "https"
META_SITE_DOMAIN = "union2018.openbudgetsindia.org" 
META_SITE_TYPE = "website"
META_SITE_NAME = "Union Budget Explorer 2018-19 - Open Budgets India"
META_INCLUDE_KEYWORDS = ["Union Budget 2018-19", "India Budget", "Budget 2018", "Union Budget", "Budget Highlights", "Budget Data", "Budget Charts", "Budget Graphs"]
META_DEFAULT_KEYWORDS = META_INCLUDE_KEYWORDS
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_TITLE_TAG = True
META_TWITTER_TYPE = "summary_large_image"
META_TWITTER_SITE = "@OpenBudgetsIn"

#Create a view which provide the template tags this value. 
HEADER_MAX_DROPDOWN_CHILDREN = 7

