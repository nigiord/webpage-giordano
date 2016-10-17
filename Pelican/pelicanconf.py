#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nils Giordano'

SITENAME = 'Nils Giordano'
SITEURL = 'http://www.normalesup.org/~giordano'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'Misc'

PATH = '../raw'
OUTPUT_PATH = '../WWW'
STATIC_PATHS = ['extra', 'images', 'pdfs', 'misc']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/htaccess': {'path': '.htaccess'}
}
RELATIVE_URLS = True

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['extract_toc','render_math','better_figures_and_images']
MD_EXTENSIONS = ['codehilite','extra','smarty', 'toc']
RESPONSIVE_IMAGES = True


# Theme configuration
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'simplex'
BOOTSTRAP_NAVBAR_INVERSE = False
FAVICON = 'extra/favicon.png'
#ABOUT_ME = '<i class="fa fa-envelope-o" aria-hidden="true"></i>\
#        <a href="http://www.google.com/recaptcha/mailhide/d?k=01vxJflfgEQgNevK72lauzLg==&amp;c=yqWFIeJ0ACeMcuh8CgQ1S3W_cX_5CqtVKYFcN1-8uUA=" onclick="window.open(\'http://www.google.com/recaptcha/mailhide/d?k\x3d01vxJflfgEQgNevK72lauzLg\x3d\x3d\x26c\x3dyqWFIeJ0ACeMcuh8CgQ1S3W_cX_5CqtVKYFcN1-8uUA\x3d', '', 'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width=500,height=300\'); return false;" title="Reveal this e-mail address">n...</a>@inria.fr\
#        <i class="fa fa-phone" aria-hidden="true"></i> +33 (0)476615300<br />\
#        <br />\
#        Inria Grenoble − Rhône-Alpes<br />\
#        Inovallée<br />\
#        655 avenue de l\'Europe<br />\
#        Montbonnot<br />\
#        38334 Saint-Ismier Cedex, France'
ABOUT_ME = '<i class="fa fa-envelope-o" aria-hidden="true"></i>\
        <script type="text/javascript" src="extra/email.js"></script>\
        <noscript>[Enable JavaScript to see my email address]</noscript><br />\
        <i class="fa fa-phone" aria-hidden="true"></i> +33 (0)476615300<br />\
        <br />\
        Inria Grenoble − Rhône-Alpes<br />\
        Inovallée<br />\
        655 avenue de l\'Europe<br />\
        Montbonnot<br />\
        38334 Saint-Ismier Cedex, France'
#AVATAR = 'images/avatar.jpg'
SIDEBAR_ONLY_ON_INDEX = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
PAGE_ORDER_BY = 'rank'
MENUITEMS = (
    ('Home', 'http://www.normalesup.org/~giordano'),
)
CC_LICENSE = 'CC-BY-NC'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Inria project-team Ibis', 'https://team.inria.fr/ibis'),
         ('Dynamic Ecology', 'https://dynamicecology.wordpress.com'),
         ('(fr) Bioinfo-fr', 'https://bioinfo-fr.net'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/nigiord'),
          ('Google Scholar', 'https://scholar.google.fr/citations?user=r4wI-i4AAAAJ'),
          ('Orcid', 'https://orcid.org/0000-0003-2549-6631'))

DEFAULT_PAGINATION = 10
LOAD_CONTENT_CACHE = False
