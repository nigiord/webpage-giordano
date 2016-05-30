#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nils Giordano'

SITENAME = 'Nils Giordano'
SITEURL = 'http://www.normalesup.org/~giordano/'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'Misc'

PATH = '../raw'
OUTPUT_PATH = '../WWW'
STATIC_PATHS = ['extra', 'images', 'pdfs']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/htaccess': {'path': '.htaccess'}
}
RELATIVE_URLS = True

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['extract_toc','render_math','better_figures_and_images']
MD_EXTENSIONS = ['codehilite','extra','smarty', 'toc']


# Theme configuration
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'simplex'
BOOTSTRAP_NAVBAR_INVERSE = False
FAVICON = 'extra/favicon.png'
ABOUT_ME = 'Computational biologist with lab skills'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (
        ('HOME', '/'),
        ('RESEARCH', '/research/overview.html'),
        ('TEACHING', '/teaching/overview.html'),
        ('BLOG', '/blog.html'),
        ('CV', '/cv.html'),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Inria', 'https://www.inria.fr'),
         ('École Normale Supérieure', 'https://www.ens.fr/'),
         ('Bioinfo-fr', 'https://bioinfo-fr.net'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/nigiord'),
          ('Google Scholar', 'https://scholar.google.fr/citations?user=r4wI-i4AAAAJ'),)

DEFAULT_PAGINATION = 10
LOAD_CONTENT_CACHE = False
