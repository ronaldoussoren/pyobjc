#!/usr/bin/env python

# Author: Bill Bumgarner
# Contact: bbum@codefab.com
# Copyright: 2002 - Bill Bumgarner - All Rights Reserved
# License: The MIT License -- see LICENSE.txt

from distutils.core import setup

setup(name = "DocArticle",
      version = "0.1",
      description = "Turn reStructuredText source into O'Reilly DevCenter compatible HTML.",
      author = "Bill Bumgarner",
      url = "mailto:bbum@codefab.com",
      author_email = "bbum@codefab.com",
      packages = ['DocArticle'],
      scripts = ['docarticle.py']
      )
