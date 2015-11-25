#!/usr/bin/env python

import setuptools
import os
import platform
from distutils.core import Command
from distutils.errors import DistutilsError


VERSION="3.1b1"

# Table with all framework wrappers and the OSX releases where they are
# first supported, and where support was removed. The introduced column
# is ``None`` when the framework is supported on OSX 10.4 or later. The
# removed column is ``None`` when the framework is present ont he latest
# supported OSX release.
FRAMEWORKS_WRAPPERS=[
        # Name                      Introcuded          Removed
        ('AVKit',                   '10.9',             None        ),
        ('AVFoundation',            '10.7',             None        ),
        ('Accounts',                '10.8',             None        ),
        ('AddressBook',             None,               None        ),
        ('AppleScriptKit',          None,               None        ),
        ('AppleScriptObjC',         '10.6',             None        ),
        ('ApplicationServices',     None,               None        ),
        ('Automator',               None,               None        ),
        ('CFNetwork',               None,               None        ),
        ('CalendarStore',           '10.5',             None        ),
        ('CloudKit',                '10.10',            None        ),
        ('Cocoa',                   None,               None        ),
        ('Collaboration',           '10.5',             None        ),
        ('Contacts',                '10.11',            None        ),
        ('ContactsUI',              '10.11',            None        ),
        ('CoreBluetooth',           '10.10',            None        ),
        ('CoreData',                None,               None        ),
        ('CoreLocation',            '10.6',             None        ),
        ('CoreText',                None,               None        ),
        ('CoreWLAN',                '10.6',             None        ),
        ('CryptoTokenKit',          '10.10',            None        ),
        ('DictionaryServices',      '10.5',             None        ),
        ('DiskArbitration',         None,               None        ),
        ('EventKit',                '10.8',             None        ),
        ('ExceptionHandling',       None,               None        ),
        ('FSEvents',                '10.5',             None        ),
        ('FinderSync',              '10.10',            None        ),
        ('GameCenter',              '10.8',             None        ),
        ('GameController',          '10.9',             None        ),
        ('IMServicePlugIn',         '10.7',             None        ),
        ('InputMethodKit',          '10.5',             None        ),
        ('ImageCaptureCore',        None,               None        ),
        ('InstallerPlugins',        None,               None        ),
        ('InstantMessage',          '10.5',             None        ),
        ('InterfaceBuilderKit',     '10.5',             '10.7'      ),
        ('LatentSemanticMapping',   None,               None        ),
        ('LaunchServices',          None,               None        ),
        ('LocalAuthentication',     '10.10',            None        ),
        ('MapKit',                  '10.9',             None        ),
        ('MediaAccessibility',      '10.9',             None        ),
        ('MediaLibrary',            '10.9',             None        ),
        ('Message',                 None,               '10.9'      ),
        ('MultipeerConnectivity',   '10.10',            None        ),
        ('NetFS',                   '10.6',             None        ),
        ('NotificationCenter',      '10.10',            None        ),
        ('OpenDirectory',           '10.6',             None        ),
        ('Photos',                  '10.11',            None        ),
        ('PhotosUI',                '10.11',            None        ),
        ('PreferencePanes',         None,               None        ),
        ('PubSub',                  '10.5',             None        ),
        ('QTKit',                   '10.5',             None        ),
        ('Quartz',                  None,               None        ),
        ('ScreenSaver',             None,               None        ),
        ('ScriptingBridge',         '10.5',             None        ),
        ('SearchKit',               None,               None        ),
        ('ServerNotification',      '10.6',             '10.9'      ),
        ('ServiceManagement',       '10.6',             None        ),
        ('Social',                  '10.8',             None        ),
        ('SpriteKit',               '10.9',             None        ),
        ('StoreKit',                '10.7',             None        ),
        ('SyncServices',            None,               None        ),
        ('SystemConfiguration',     None,               None        ),
        ('WebKit',                  None,               None        ),
        ('XgridFoundation',         None,               '10.8'      ),
#        ('AudioVideoBridging',      '10.8',             None        ),
#        ('GLKit',                   '10.8',             None        ),
#        ('GameKit',                 '10.8',             None        ),
#        ('MediaToolbox',            '10.8',             None        ),
        ('SceneKit',                '10.7',             None        ),
#        ('SpriteKit',               '10.9',             None        ),
#        ('VideoToolbox',            '10.8',             None        ),
]


BASE_REQUIRES=[
        'py2app>=0.10',
        'pyobjc-core=='+VERSION,
]

def version_key(version):
    return tuple(int(x) for x in version.split('.'))

def framework_requires():
    build_platform = platform.mac_ver()[0]
    result = []

    for name, introduced, removed in FRAMEWORKS_WRAPPERS:
        if introduced is not None and version_key(introduced) > version_key(build_platform):
            continue
        if removed is not None and version_key(removed) <= version_key(build_platform):
            continue

        result.append('pyobjc_framework-%s=='%(name,)+VERSION)

    return result


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
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.1
Programming Language :: Python :: 3.2
Programming Language :: Python :: 3.3
Programming Language :: Objective C
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: User Interfaces
""".splitlines())


class oc_test (Command):
    description = "run test suite"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        all_names = set(nm.split('-')[-1] for nm in os.listdir('..') if nm.startswith('pyobjc-framework-'))
        configured_names = set(x[0] for x in FRAMEWORKS_WRAPPERS)
        ok = True
        if all_names - configured_names:
            print("Framework wrappers not mentioned in setup.py: %s"%(", ".join(all_names - configured_names)))
            ok = False
        if configured_names - all_names:
            print("Framework mentioned in setup.py not in filesystem: %s"%(", ".join(configured_names - all_names)))
            ok = False

        if not ok:
           raise DistutilsError("setup.py is not consistent with reality")

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
    install_requires = BASE_REQUIRES + framework_requires(),
    setup_requires = [],
    extra_path = "PyObjC",
    classifiers = CLASSIFIERS,
    license = 'MIT License',
    zip_safe = True,
    # workaround for setuptools 0.6b4 bug
    dependency_links = [],
    keywords=['Objective-C', 'bridge', 'Cocoa'],
    cmdclass={
        'test': oc_test
    },
)
