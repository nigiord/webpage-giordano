#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nils Giordano'

SITENAME = "Nils Giordano"
SITEURL = 'https://www.normalesup.org/~giordano'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
#DEFAULT_CATEGORY = 'Misc'

PATH = 'Raw'
OUTPUT_PATH = 'WWW'
STATIC_PATHS = ['extra', 'images', 'pdfs']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/htaccess': {'path': '.htaccess'},
    'extra/custom.css': {'path': 'static/custom.css'}
}
RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites',
           'pelican_resume',
           'pelican-bootstrapify']

MARKDOWN = {
        'extension_configs': {
                    'markdown.extensions.codehilite': {'css_class': 'highlight'},
                    'markdown.extensions.extra': {},
                    'markdown.extensions.smarty': {},
                    'markdown.extensions.toc': {},
                },
        'output_format': 'html5',
}
RESPONSIVE_IMAGES = True
HIDE_SIDEBAR = True
#BANNER = 'extra/kastarpowa.gif'
BANNER_ALL_PAGES = True
BANNER_ONLY = True

# Configuration for the pelican-resume plugin that generate pdf for CV
RESUME_SRC = 'pages/cv.md'
RESUME_PDF = 'pdfs/cv_giordano.pdf'

# Theme configuration
THEME = '../pelican-themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_SUBSITES = {'fr': {}}
BOOTSTRAP_THEME = 'spacelab'
CUSTOM_CSS = 'static/custom.css'
BOOTSTRAP_NAVBAR_INVERSE = False
SIDEBAR_ONLY_ON_INDEX = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
PAGES_SORT_ATTRIBUTE = 'rank'
MENUITEMS = (
    ('Home', './'),
)
CC_LICENSE = 'CC-BY-NC'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('ComBi team', 'https://www.ls2n.fr/equipe/combi/'),
    ('PeerCommunityIn', 'https://peercommunityin.org/'),
    ('Dynamic Ecology', 'https://dynamicecology.wordpress.com'),
    ('(fr) Bioinfo-fr', 'https://bioinfo-fr.net'),
)

# Social widget
SOCIAL = (('Github', 'https://github.com/nigiord'),
          ('Google Scholar', 'https://scholar.google.fr/citations?user=r4wI-i4AAAAJ'),
          ('Orcid', 'https://orcid.org/0000-0003-2549-6631'),
          ('CV', 'pdfs/cv_giordano.pdf')
         )
INCLUDE_SOCIAL_IN_NAVBAR = True

#GITHUB_USER = 'nigiord'
DEFAULT_PAGINATION = 10
LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = True
