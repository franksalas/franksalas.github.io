#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Francisco Salas'
SITENAME = 'salas'
SITEURL = ''

#PATH = 'content'
ARTICLE_DIRS = ['articles']

STATIC_PATHS = ['images','extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}



TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
          ('linkedin', 'https://www.linkedin.com/in/frank-salas/'),
          ('github', 'http://github.com/franksalas'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

### Themes ###
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# THEME and variables
THEME = './themes/salasClean'

SHOW_ARCHIVES = False
SHOW_TAGS = False





#### Plugins ####
MARKUP = ('md', 'ipynb')
#MARKUP = ('md',)

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}





PLUGIN_PATHS = ['./plugins']
#PLUGINS = ['render_math','ipynb.markup','ipynb.liquid','liquid_tags.img']

PLUGINS = ['render_math',
            'ipynb.markup',
            'ipynb.liquid',
            'liquid_tags.img',
            'liquid_tags.giphy',
            'liquid_tags.graphviz',
            'liquid_tags.youtube']



IPYNB_IGNORE_CSS=True



MATH_JAX = {'color':'black','align':'center'}


GIPHY_API_KEY = 'HA14SwsBeXdWSivIrB0pfEDNUjbaXcFM'