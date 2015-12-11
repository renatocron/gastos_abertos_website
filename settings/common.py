# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#
# Common settings
#

AVAILABLE_LOCALES = ['pt_BR', 'en']

DEBUG = True
DEFAULT_LOCALE = 'pt_BR'

FLATPAGES_PAGES_AUTO_RELOAD = DEBUG
FLATPAGES_PAGES_EXTENSION = '.md'
FLATPAGES_PAGES_ROOT = '../content/pages'

FLATPAGES_BLOG_AUTO_RELOAD = DEBUG
FLATPAGES_BLOG_EXTENSION = '.md'
FLATPAGES_BLOG_ROOT = '../content/blog'

FLATPAGES_AUTHORS_AUTO_RELOAD = DEBUG
FLATPAGES_AUTHORS_EXTENSION = '.md'
FLATPAGES_AUTHORS_ROOT = '../content/authors'

FREEZER_DESTINATION = '../build'

BABEL_DEFAULT_LOCALE = DEFAULT_LOCALE

API_URL = 'http://api.gastosabertos.org'
