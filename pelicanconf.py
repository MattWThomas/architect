#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Matthew Thomas'
SITENAME = 'Architect theme'
SITEDESCRIPTION = 'Architect is a theme for GitHub Pages.'
SITEURL = '/architect-pelican'

# GitHub Repo Properties (type: project/user)
GITHUB = {
    'repo' : 'MattWThomas/architect-pelican',
    'branch': 'master',
    'downloads': True
}

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Set theme
THEME = 'themes/architect'

# Load plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets']

# Let the assets plugin deal with css
IGNORE_FILES = ['*.css']

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Google analytics ID
# GOOGLE_ANALYTICS = 