#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()

import os

VERSION='2.2b3'

# NOTE: This list of requirements is split into sections for 10.4
# and 10.5 to make it possible to install PyObjC from source on all
# supported platforms.
REQUIRES=[
# The line below won't install py2app for some reason and I have no
# idea why that's so.
#        'py2app==dev,>=0.4',
        'pyobjc-core=='+VERSION,
#       'pyobjc-metadata',
        'pyobjc-framework-AddressBook=='+VERSION,
        'pyobjc-framework-AppleScriptKit=='+VERSION,
        'pyobjc-framework-Automator=='+VERSION,
        'pyobjc-framework-CFNetwork=='+VERSION,
        'pyobjc-framework-Cocoa=='+VERSION,
        'pyobjc-framework-CoreData=='+VERSION,
        'pyobjc-framework-CoreText=='+VERSION,
        'pyobjc-framework-ExceptionHandling=='+VERSION,
        'pyobjc-framework-FSEvents=='+VERSION,
        'pyobjc-framework-InstallerPlugins=='+VERSION,
        'pyobjc-framework-LatentSemanticMapping=='+VERSION,
#        'pyobjc-framework-LaunchServices=='+VERSION,
        'pyobjc-framework-Message=='+VERSION,
        'pyobjc-framework-PreferencePanes=='+VERSION,
        'pyobjc-framework-Quartz=='+VERSION,
        'pyobjc-framework-ScreenSaver=='+VERSION,
        'pyobjc-framework-SearchKit=='+VERSION,
        'pyobjc-framework-SyncServices=='+VERSION,
        'pyobjc-framework-SystemConfiguration=='+VERSION,
        'pyobjc-framework-WebKit=='+VERSION,
        'pyobjc-framework-XgridFoundation=='+VERSION,
]
REQUIRES_10_5=[
        'pyobjc-framework-CalendarStore=='+VERSION,
        'pyobjc-framework-Collaboration=='+VERSION,
        'pyobjc-framework-DictionaryServices=='+VERSION,
        'pyobjc-framework-InputMethodKit=='+VERSION,
        'pyobjc-framework-InstantMessage=='+VERSION,
        'pyobjc-framework-InterfaceBuilderKit=='+VERSION,
        'pyobjc-framework-PubSub=='+VERSION,
        'pyobjc-framework-QTKit=='+VERSION,
        'pyobjc-framework-ScriptingBridge=='+VERSION,
]

import platform
rel = map(int, platform.mac_ver()[0].split('.')[:2])
if rel >= (10, 5):
    REQUIRES.extend(REQUIRES_10_5)

# Some PiPy stuff
LONG_DESCRIPTION="""
PyObjC is a bridge between Python and Objective-C.  It allows full
featured Cocoa applications to be written in pure Python.  It is also
easy to use other frameworks containing Objective-C class libraries
from Python and to mix in Objective-C, C and C++ source.

This package is a pseudo-package that will install all pyobjc related
packages (that is, pyobjc-core as well as wrapppers for frameworks on
OSX)
"""

from setuptools import setup, Extension, find_packages
import os


CLASSIFIERS = filter(None,
"""
Development Status :: 5 - Production/Stable
Environment :: Console
Environment :: MacOS X :: Cocoa
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: MacOS :: MacOS X
Programming Language :: Python
Programming Language :: Objective C
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: User Interfaces
""".splitlines())

dist = setup(
    name = "pyobjc", 
    version = VERSION,
    description = "Python<->ObjC Interoperability Module",
    long_description = LONG_DESCRIPTION,
    author = "Ronald Oussoren",
    author_email = "pyobjc-dev@lists.sourceforge.net",
    url = "http://pyobjc.sourceforge.net/",
    platforms = [ 'MacOS X' ],
    packages = [],
    install_requires = REQUIRES,
    setup_requires = [],
    extra_path = "PyObjC",
    classifiers = CLASSIFIERS,
    license = 'MIT License',
    zip_safe = True,
    # workaround for setuptools 0.6b4 bug
    dependency_links = [],
)
