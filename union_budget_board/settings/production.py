from .base import *

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DEBUG = False

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': '/home/cbga/ubb/project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}
ALLOWED_HOSTS = ["union2018.openbudgetsindia.org"]

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