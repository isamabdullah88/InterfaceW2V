"""
WSGI config for InterfaceW2V project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/word2visual/Neuro-Flash/Word2Visuals/InterfaceW2V/')
sys.path.append('/home/word2visual/Neuro-Flash/Word2Visuals/VEnv/Lib/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "InterfaceW2V.settings")

application = get_wsgi_application()
