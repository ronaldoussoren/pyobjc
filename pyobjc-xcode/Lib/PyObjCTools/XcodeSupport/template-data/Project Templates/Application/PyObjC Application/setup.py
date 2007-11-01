#!/usr/bin/env python
#
# ------------------------------------------------
#
#   CHANGE ABOVE OR EDIT THE "Shell Script Files"
#   PHASE TO START THE THIS SCRIPT WITH ANOTHER
#   PYTHON INTERPRETER.
#
# ------------------------------------------------
# 

"""
Distutils script for building ÇPROJECTNAMEÈ.

Development:
    xcodebuild -buildstyle Development

Deployment:
    xcodebuild -buildstyle Deployment

These will place the executable in
the "build" dir by default.

Alternatively, you can use py2app directly.
    
Development:
    python setup.py py2app --alias
    
Deployment:
    python setup.py py2app
    
These will place the executable in
the "dist" dir by default.

"""

from distutils.core import setup
import py2app
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from PyObjCTools import XcodeSupport

xcode = XcodeSupport.xcodeFromEnvironment(
    'ÇPROJECTNAMEASIDENTIFIERÈ.xcode',
    os.environ,
)

sys.argv = xcode.py2app_argv(sys.argv)
setup_options = xcode.py2app_setup_options('app')

#
# mangle any distutils options you need here
# in the setup_options dict
#

setup(**setup_options)
