#!/usr/bin/env python
"""
A couple of useful modules from the (Mac)Python CVS tree. They are
necessary to build .app bundles using python scripts (e.g.
Examples/TableModel/buildpyapp.py).

There are two reasons they are included here:
a) They're not available in Python 2.2
b) They're not installed by default in a static (non-framework) build
   of CVS Python. Note: this is (probably/hopefully) going to change
   before the release of Python 2.3.

So: install these only if either of the above situations apply to you.
"""

from distutils.core import setup

setup(name = "pyobjc-macpython",
      version = '0.1',
      description = "PyObjC: Modules borrowed from MacPython",
      author_email = "pyobjc-dev@lists.sourceforge.net",
      url = "http://pyobjc.sourceforge.net/",
      py_modules = ['bundlebuilder', 'plistlib'],
      package_dir = {'': ''},
)
