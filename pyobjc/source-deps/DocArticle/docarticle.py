#!/usr/bin/env python

# Author: Bill Bumgarner
# Contact: bbum@codefab.com
# Copyright: This module has been placed in the public domain.

"""
docarticle.py
=============

This module provides a simple command line interface that uses the
DocArticle HTML writer to produce plain HTML output from
ReStructuredText source.
"""

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description
from DocArticle import DocArticleWriter

description = ("Generates plain HTML.  " + default_description)

publish_cmdline(writer=DocArticleWriter(), description=description)
