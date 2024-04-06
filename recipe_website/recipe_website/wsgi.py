"""
WSGI config for recipe_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

from dotenv import load_dotenv

project_folder = os.path.expanduser('~/Recept2') # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

## assuming your django settings file is at '/home/Proninlek13/mysite/mysite/settings.py'
## and your manage.py is is at '/home/Proninlek13/mysite/manage.py'
path = '/home/Proninlek13/recipe_website'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'recipe_website.settings'

## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
