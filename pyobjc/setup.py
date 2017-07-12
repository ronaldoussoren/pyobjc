#!/usr/bin/env python

import setuptools
import os
import platform
from distutils.core import Command
from distutils.errors import DistutilsError

import shutil
import subprocess
import glob
import tarfile
import sys
import ast

VERSION="3.3a0"

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
        ('ColorSync',               '10.13',            None        ),
        ('Contacts',                '10.11',            None        ),
        ('ContactsUI',              '10.11',            None        ),
        ('CoreBluetooth',           '10.10',            None        ),
        ('CoreData',                None,               None        ),
        ('CoreLocation',            '10.6',             None        ),
        ('CoreML',                  '10.13',            None        ),
        ('CoreServices',            None,               None        ),
        #('CoreSpotlight',           '10.13',            None        ),
        ('CoreText',                None,               None        ),
        ('CoreWLAN',                '10.6',             None        ),
        ('CryptoTokenKit',          '10.10',            None        ),
        ('DictionaryServices',      '10.5',             None        ),
        ('DiskArbitration',         None,               None        ),
        ('EventKit',                '10.8',             None        ),
        ('ExceptionHandling',       None,               None        ),
        ('ExternalAccessory',       '10.13',            None        ),
        ('FSEvents',                '10.5',             None        ),
        ('FinderSync',              '10.10',            None        ),
        ('GameCenter',              '10.8',             None        ),
        ('GameController',          '10.9',             None        ),
        ('IMServicePlugIn',         '10.7',             None        ),
        ('InputMethodKit',          '10.5',             None        ),
        ('ImageCaptureCore',        None,               None        ),
        ('Intents',                 '10.12',            None        ),
        ('InstallerPlugins',        None,               None        ),
        ('InstantMessage',          '10.5',             None        ),
        ('InterfaceBuilderKit',     '10.5',             '10.7'      ),
        ('IOSurface',               '10.6',             None        ),
        ('LatentSemanticMapping',   None,               None        ),
        ('LaunchServices',          None,               None        ),
        ('LocalAuthentication',     '10.10',            None        ),
        ('MapKit',                  '10.9',             None        ),
        ('MediaAccessibility',      '10.9',             None        ),
        ('MediaLibrary',            '10.9',             None        ),
        ('MediaPlayer',             '10.12',            None        ),
        ('Message',                 None,               '10.9'      ),
        ('ModelIO',                 '10.11',            None        ),
        ('MultipeerConnectivity',   '10.10',            None        ),
        ('NetFS',                   '10.6',             None        ),
        ('NetworkExtension',        '10.11',            None        ),
        ('NotificationCenter',      '10.10',            None        ),
        ('OpenDirectory',           '10.6',             None        ),
        ('Photos',                  '10.11',            None        ),
        ('PhotosUI',                '10.11',            None        ),
        ('PreferencePanes',         None,               None        ),
        ('PubSub',                  '10.5',             None        ),
        ('QTKit',                   '10.5',             None        ),
        ('Quartz',                  None,               None        ),
        ('SafariServices',          '10.11',            None        ),
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
#        ('Vision',                  '10.13',            None        ),

        # iTunes library is shipped with iTunes, not part of macOS 'core'
        ('iTunesLibrary',           None,               None        ),
]


BASE_REQUIRES=[
        'pyobjc-core=='+VERSION,
]

def version_key(version):
    return tuple(int(x) for x in version.split('.'))

def framework_requires():
    if sys.platform != 'darwin':
        raise SystemExit("ERROR: Requires macOS to install or build")

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
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Objective C
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: User Interfaces
""".splitlines())

_SETUP_KEYS=(
    'name',
    'description',
    'min_os_level',
    'max_os_level',
    'packages',
    'namespace_packages',
    'ext_modules',
    'version',
    'install_requires',
    'long_description',
)
_SETUP_OPTIONAL=(
    'min_os_level',
    'max_os_level',
    'ext_modules',
    'namespace_packages',
)

def same_order(lst1, lst2):
    idx = 0
    for k in lst1:
        try:
            while lst2[idx] != k:
                idx+=1
        except IndexError:
            return False
    return True

class oc_test (Command):
    description = "run test suite"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("  validating framework list...")
        all_names = set(nm.split('-')[-1] for nm in os.listdir('..') if nm.startswith('pyobjc-framework-'))
        configured_names = set(x[0] for x in FRAMEWORKS_WRAPPERS)
        ok = True
        if all_names - configured_names:
            print("Framework wrappers not mentioned in setup.py: %s"%(", ".join(all_names - configured_names)))
            ok = False
        if configured_names - all_names:
            print("Framework mentioned in setup.py not in filesystem: %s"%(", ".join(configured_names - all_names)))
            ok = False

        print("  validating framework Modules/ directories...")
        header_files = ("pyobjc-api.h", "pyobjc-compat.h")
        templates = {}
        for fn in header_files:
            with open(os.path.join('../pyobjc-core/Modules/objc', fn), 'rb') as fp:
                templates[fn] = fp.read()

        for nm in all_names:
            subdir = "../pyobjc-framework-" + nm + "/Modules"
            if not os.path.exists(subdir): continue

            for fn in header_files:
                if not os.path.exists(os.path.join(subdir, fn)):
                    print("Framework wrapper for %s does not contain %s"%(
                        nm, fn))
                    ok = False

                else:
                    with open(os.path.join(subdir, fn), 'rb') as fp:
                        data = fp.read()

                    if data != templates[fn]:
                        print("Framework wrapper for %s contains stale %s"%(
                            nm, fn))
                        ok = False


        print("  validating framework setup files...")
        with open('../pyobjc-core/Tools/pyobjc_setup.py', 'rb') as fp:
            pyobjc_setup = fp.read()

        for nm in sorted(all_names):
            subdir = "../pyobjc-framework-" + nm
            if not os.path.exists(os.path.join(subdir, "MANIFEST.in")):
                print("Framework wrapper for %s does not contain MANIFEST.in"%(
                    nm))
                ok = False

            if not os.path.exists(os.path.join(subdir, "setup.py")):
                print("Framework wrapper for %s does not contain setup.py"%(
                    nm))
                ok = False

            if not os.path.exists(os.path.join(subdir, "pyobjc_setup.py")):
                print("Framework wrapper for %s does not contain pyobjc_setup.py"%(
                    nm))
                ok = False

            else:
                with open(os.path.join(subdir, "pyobjc_setup.py"), 'rb') as fp:
                    data = fp.read()
                if data != pyobjc_setup:
                    print("Framework wrapper for %s contains stale pyobjc_setup.py"%(
                        nm))
                    ok = False

            if not os.path.exists(os.path.join(subdir, "setup.py")):
                print("Framework wrapper for %s does not contain setup.py"%(nm))
                ok = False
            else:
                with open(os.path.join(subdir, "setup.py")) as fp:
                    contents = fp.read()

                if "setup_requires" in contents:
                    print("Framework wrapper for %s has setup_requires"%(nm))
                    ok = False

                a = compile(contents, subdir, 'exec', ast.PyCF_ONLY_AST)
                try:
                    args = [ v.arg for v in a.body[-1].value.keywords ]

                    if a.body[-1].value.func.id != 'setup':
                        print("Unexpected setup.py structure in wrapper for %s"%(nm))
                        ok = False

                    elif a.body[-1].value.args:
                        print("Unexpected setup.py structure in wrapper for %s"%(nm))

                    for n in a.body:
                        if isinstance(n, ast.Assign):
                            if n.targets[0].id == 'VERSION':
                                found_version = n.value.s

                except AttributeError:
                    print("Unexpected setup.py structure in wrapper for %s"%(nm))
                    ok = False

                if not same_order(args, _SETUP_KEYS):
                    print("Unexpected order of setup.py keyword args in wrapper for %s"%(nm,))
                    ok = False

                for k in set(_SETUP_KEYS) - set(_SETUP_OPTIONAL):
                    if k not in args:
                        print("Missing %r in setup.py keyword args in wrapper for %s"%(k, nm,))
                        ok = False

                if 'ext_modules' not in args:
                    if os.path.exists(os.path.join(subdir, 'Modules')):
                        print("No ext_modules in setup.py, but Modules subdir, in wrapper for %s"%(nm,))
                        ok = False


                if found_version != VERSION:
                    print("Bad version in wrapper for %s"%(nm,))
                    ok = False

        devnull = open('/dev/null', 'a')
        for nm in ('pyobjc-core',) + tuple(nm for nm in os.listdir('..') if nm.startswith('pyobjc-framework-')):
            print("    %s"%(nm,))
            subdir = os.path.join('..', nm)
            if os.path.exists(os.path.join(subdir, 'dist')):
                shutil.rmtree(os.path.join(subdir, 'dist'))
                p = subprocess.check_call(
                    [ sys.executable, 'setup.py', 'sdist' ],
                    cwd=subdir,
                    stdout=devnull, stderr=devnull
                    )
                files = glob.glob(
                    os.path.join(subdir, 'dist', '*.tar.gz'))

                if not files:
                    print("No sdist in %s"%(nm,))
                    ok = False

                elif len(files) > 1:
                    print("Too many sdist in %s"%(nm,))
                    ok = False

                else:
                    t = tarfile.open(files[0], 'r:gz')
                    for fn in t.getnames():
                        if fn.startswith('/'):
                            print("Absolute path in sdist for %s"%(nm,))
                            ok = False

                        for p in (
                            '__pycache__', '.pyc', '.pyo', '.so',
                            '.dSYM', '.eggs', '.app', '/build/', '/dist/'):

                            if p in fn:
                                print("Unwanted pattern %r in sdist for %s: %s"%(
                                    p, nm, fn))
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
    platforms = [ 'macOS' ],
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
