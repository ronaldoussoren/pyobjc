#!/usr/bin/env python
"""
A number of usefull modules from MacPython. These are necessary to build
.app bundles using python scripts (e.g. Examples/TableModel/buildpyapp.py)

Install this only if you do not have a MacPython installation!
"""

from distutils.core import setup

setup (name = "pyobjc-macpython",
          version = '0.1',
           description = "PyObjC: Modules borrowed from MacPython",
           author_email = "pyobjc-dev@lists.sourceforge.net",
	   url = "http://pyobjc.sourceforge.net/",
           py_modules = [ 'bundlebuilder', 'plistlib' ],
           package_dir = { '': '' },
           )


