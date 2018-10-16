#!/usr/bin/env python

import setuptools
import os
import platform
from distutils.core import Command
from distutils.errors import DistutilsError
from setuptools.command import egg_info

import shutil
import subprocess
import glob
import tarfile
import sys
import ast

VERSION="5.1"

# Table with all framework wrappers and the OSX releases where they are
# first supported, and where support was removed. The introduced column
# is ``None`` when the framework is supported on OSX 10.4 or later. The
# removed column is ``None`` when the framework is present ont he latest
# supported OSX release.
FRAMEWORK_WRAPPERS=[
        # Name                      Introcuded          Removed
        ('libdispatch',             '10.8',             None        ),
        ('AdSupport',               '10.14',            None        ),
        ('AVKit',                   '10.9',             None        ),
        ('AVFoundation',            '10.7',             None        ),
        ('Accounts',                '10.8',             None        ),
        ('AddressBook',             None,               None        ),
        ('AppleScriptKit',          None,               None        ),
        ('AppleScriptObjC',         '10.6',             None        ),
        ('ApplicationServices',     None,               None        ),
        ('Automator',               None,               None        ),
        ('BusinessChat',            '10.14',            None        ),
        ('CFNetwork',               None,               None        ),
        ('CalendarStore',           '10.5',             None        ),
        ('CloudKit',                '10.10',            None        ),
        ('Cocoa',                   None,               None        ),
        ('Collaboration',           '10.5',             None        ),
        ('ColorSync',               '10.13',            None        ),
        ('Contacts',                '10.11',            None        ),
        ('ContactsUI',              '10.11',            None        ),
        ('CoreAudio',               None,               None        ),
        ('CoreAudioKit',            None,               None        ),
        ('CoreBluetooth',           '10.10',            None        ),
        ('CoreData',                None,               None        ),
        ('CoreLocation',            '10.6',             None        ),
        ('CoreMedia',               '10.7',             None        ),
        ('CoreMediaIO',             '10.7',             None        ),
        #('CoreMIDI',                None,               None        ),
        ('CoreML',                  '10.13',            None        ),
        ('CoreServices',            None,               None        ),
        ('CoreSpotlight',           '10.13',            None        ),
        ('CoreText',                None,               None        ),
        ('CoreWLAN',                '10.6',             None        ),
        ('CryptoTokenKit',          '10.10',            None        ),
        ('DictionaryServices',      '10.5',             None        ),
        ('DiscRecording',           None,               None        ),
        ('DiscRecordingUI',         None,               None        ),
        ('DiskArbitration',         None,               None        ),
        ('DVDPlayback',             None,               None        ),
        ('EventKit',                '10.8',             None        ),
        ('ExceptionHandling',       None,               None        ),
        ('ExternalAccessory',       '10.13',            None        ),
        ('FSEvents',                '10.5',             None        ),
        ('FinderSync',              '10.10',            None        ),
        ('GameCenter',              '10.8',             None        ),
        ('GameController',          '10.9',             None        ),
        ('IMServicePlugIn',         '10.7',             None        ),
        ('InputMethodKit',          '10.5',             None        ),
        ('ImageCaptureCore',        '10.6',             None        ),
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
        ('MediaToolbox',            '10.9',             None        ),
        ('Message',                 None,               '10.9'      ),
        ('ModelIO',                 '10.11',            None        ),
        ('MultipeerConnectivity',   '10.10',            None        ),
        ('NaturalLanguage',         '10.14',            None        ),
        ('NetFS',                   '10.6',             None        ),
        ('Network',                 '10.14',            None        ),
        ('NetworkExtension',        '10.11',            None        ),
        ('NotificationCenter',      '10.10',            None        ),
        ('OpenDirectory',           '10.6',             None        ),
        ('OSAKit',                  None,               None        ),
        ('Photos',                  '10.11',            None        ),
        ('PhotosUI',                '10.11',            None        ),
        ('PreferencePanes',         None,               None        ),
        ('PubSub',                  '10.5',             None        ),
        ('QTKit',                   '10.5',             None        ),
        ('Quartz',                  None,               None        ),
        ('SafariServices',          '10.11',            None        ),
        ('ScreenSaver',             None,               None        ),
        ('ScriptingBridge',         '10.5',             None        ),
        ('Security',      	    None,               None        ),
        ('SecurityFoundation',      None,               None        ),
        ('SecurityInterface',       None,               None        ),
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
        ('GameKit',                 '10.8',             None        ),
        ('GameplayKit',             '10.11',            None        ),
        ('SceneKit',                '10.7',             None        ),
        ('UserNotifications',       '10.14',            None        ),
        ('VideoSubscriberAccount',  '10.14',            None        ),
        ('VideoToolbox',            '10.8',             None        ),
        ('Vision',                  '10.13',            None        ),

        # iTunes library is shipped with iTunes, not part of macOS 'core'
	# Requires iTunes 11 or later, which is not available on 10.5
        ('iTunesLibrary',           '10.6',             None        ),
]

MACOS_TO_DARWIN = {
        '10.2': '6.0',
        '10.3': '7.0',
        '10.4': '8.0',
        '10.5': '9.0',
        '10.6': '10.0',
        '10.7': '11.0',
        '10.8': '12.0',
        '10.9': '13.0',
        '10.10': '14.0',
        '10.11': '15.0',
        '10.12': '16.0',
        '10.13': '17.0',
        '10.14': '18.0',
}


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

    for name, introduced, removed in FRAMEWORK_WRAPPERS:

        marker = []
        if introduced is not None:
            marker.append('platform_release>="%s"'%(MACOS_TO_DARWIN[introduced],))

        if removed is not None:
            marker.append('platform_release<"%s"'%(MACOS_TO_DARWIN[removed],))

        if marker:
            marker = ';%s'%(' and '.join(marker),)
        else:
            marker = ''

        result.append('pyobjc-framework-%s==%s%s'%(name,VERSION,marker))

    return result


# Some PyPI stuff
LONG_DESCRIPTION="""
PyObjC is a bridge between Python and Objective-C.  It allows full
featured Cocoa applications to be written in pure Python.  It is also
easy to use other frameworks containing Objective-C class libraries
from Python and to mix in Objective-C, C and C++ source.

This package is a pseudo-package that will install all pyobjc related
packages (that is, pyobjc-core as well as wrappers for frameworks on
macOS)

Project links
-------------

* `Documentation <https://pyobjc.readthedocs.io/en/latest/>`_
* `Issue Tracker <https://bitbucket.org/ronaldoussoren/pyobjc/issues?status=new&status=open>`_
* `Repository <https://bitbucket.org/ronaldoussoren/pyobjc/>`_
"""

from setuptools import setup, Extension, find_packages
import os


CLASSIFIERS = list(filter(None,
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
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Objective C
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: User Interfaces
""".splitlines()))

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
    user_options = [
        ('verbosity=', None, "print what tests are run"),
    ]

    def initialize_options(self):
        self.verbosity=1

    def finalize_options(self):
        if isinstance(self.verbosity, str):
            self.verbosity=int(self.verbosity)

    def run(self):
        try:
            import readme_renderer
        except ImportError:
            readme_renderer = None


        print("  validating framework list...")
        all_names = set(nm.split('-')[-1] for nm in os.listdir('..') if nm.startswith('pyobjc-framework-'))
        configured_names = set(x[0] for x in FRAMEWORK_WRAPPERS)
        failures = 0

        if all_names - configured_names:
            print("Framework wrappers not mentioned in setup.py: %s"%(", ".join(sorted(all_names - configured_names))))
            failures += 1
        if configured_names - all_names:
            print("Framework mentioned in setup.py not in filesystem: %s"%(", ".join(sorted(configured_names - all_names))))
            failures += 1

        print("  validating framework Modules/ directories...")
        header_files = ("pyobjc-api.h", "pyobjc-compat.h")
        templates = {}
        for fn in header_files:
            with open(os.path.join('../pyobjc-core/Modules/objc', fn), 'rb') as fp:
                templates[fn] = fp.read()

        for nm in sorted(all_names):
            subdir = "../pyobjc-framework-" + nm + "/Modules"
            if not os.path.exists(subdir): continue

            for fn in header_files:
                if not os.path.exists(os.path.join(subdir, fn)):
                    print("Framework wrapper for %s does not contain %s"%(
                        nm, fn))
                    failures += 1

                else:
                    with open(os.path.join(subdir, fn), 'rb') as fp:
                        data = fp.read()

                    if data != templates[fn]:
                        print("Framework wrapper for %s contains stale %s"%(
                            nm, fn))
                        failures += 1


        print("  validating framework setup files...")
        with open('../pyobjc-core/Tools/pyobjc_setup.py', 'rb') as fp:
            pyobjc_setup = fp.read()

        for nm in sorted(all_names):
            subdir = "../pyobjc-framework-" + nm
            if not os.path.exists(os.path.join(subdir, "MANIFEST.in")):
                print("Framework wrapper for %s does not contain MANIFEST.in"%(
                    nm))
                failures += 1

            if not os.path.exists(os.path.join(subdir, "License.txt")):
                print("Framework wrapper for %s does not contain MANIFEST.in"%(
                    nm))
                failures += 1

            if not os.path.exists(os.path.join(subdir, "setup.py")):
                print("Framework wrapper for %s does not contain setup.py"%(
                    nm))
                failures += 1

            if not os.path.exists(os.path.join(subdir, "pyobjc_setup.py")):
                print("Framework wrapper for %s does not contain pyobjc_setup.py"%(
                    nm))
                failures += 1

            else:
                with open(os.path.join(subdir, "pyobjc_setup.py"), 'rb') as fp:
                    data = fp.read()
                if data != pyobjc_setup:
                    print("Framework wrapper for %s contains stale pyobjc_setup.py"%(
                        nm))
                    failures += 1

            if not os.path.exists(os.path.join(subdir, "setup.py")):
                print("Framework wrapper for %s does not contain setup.py"%(nm))
                failures += 1
            else:
                with open(os.path.join(subdir, "setup.py")) as fp:
                    contents = fp.read()

                if "setup_requires" in contents:
                    print("Framework wrapper for %s has setup_requires"%(nm))
                    failures += 1

                a = compile(contents, subdir, 'exec', ast.PyCF_ONLY_AST)
                try:
                    args = [ v.arg for v in a.body[-1].value.keywords ]

                    if a.body[-1].value.func.id != 'setup':
                        print("Unexpected setup.py structure in wrapper for %s"%(nm))
                        failures += 1

                    elif a.body[-1].value.args:
                        print("Unexpected setup.py structure in wrapper for %s"%(nm))
                        failures += 1

                    for n in a.body:
                        if isinstance(n, ast.Assign):
                            if n.targets[0].id == 'VERSION':
                                found_version = n.value.s

                except AttributeError:
                    print("Unexpected setup.py structure in wrapper for %s"%(nm))
                    failures += 1

                if not same_order(args, _SETUP_KEYS):
                    print("Unexpected order of setup.py keyword args in wrapper for %s"%(nm,))
                    failures += 1

                for k in set(_SETUP_KEYS) - set(_SETUP_OPTIONAL):
                    if k not in args:
                        print("Missing %r in setup.py keyword args in wrapper for %s"%(k, nm,))
                        failures += 1

                if 'ext_modules' not in args:
                    if os.path.exists(os.path.join(subdir, 'Modules')):
                        print("No ext_modules in setup.py, but Modules subdir, in wrapper for %s"%(nm,))
                        failures += 1


                if found_version != VERSION:
                    print("Bad version in wrapper for %s"%(nm,))
                    failures += 1

        if readme_renderer is None:
            print("  NOT validating long description")

        else:
            print("  validating long description...")
            for nm in ('pyobjc', 'pyobjc-core',) + tuple(sorted(nm for nm in os.listdir('..') if nm.startswith('pyobjc-framework-'))):
                subdir = os.path.join('..', nm)
                if readme_renderer is not None:
                    print("    %s"%(nm,))
                    try:
                        subprocess.check_output([sys.executable, 'setup.py', 'check', '-r', '-s'], cwd=subdir)
                    except subprocess.CalledProcessError:
                        failures += 1

        print("  validating sdist archives...")
        devnull = open('/dev/null', 'a')
        for nm in ('pyobjc-core',) + tuple(sorted(nm for nm in os.listdir('..') if nm.startswith('pyobjc-framework-'))):
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
                    failures += 1

                elif len(files) > 1:
                    print("Too many sdist in %s"%(nm,))
                    failures += 1

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
                                failures += 1

        print("SUMMARY: {'testSeconds': 0.0, 'count': 0, 'fails': %d, 'errors': 0, 'xfails': 0, 'skip': 0, 'xpass': 0, }"%(failures,))
        if failures:
            sys.exit(1)


class oc_egg_info (egg_info.egg_info):
    def run(self):
        egg_info.egg_info.run(self)

        path = os.path.join(self.egg_info, 'PKG-INFO')
        with open(path, 'a+') as fp:
            fp.write('Project-URL: Documentation, https://pyobjc.readthedocs.io/en/latest/\n')
            fp.write('Project-URL: Issue tracker, https://bitbucket.org/ronaldoussoren/pyobjc/issues?status=new&status=open\n')


dist = setup(
    name = "pyobjc",
    version = VERSION,
    description = "Python<->ObjC Interoperability Module",
    long_description = LONG_DESCRIPTION,
    long_description_content_type = 'text/x-rst; charset=UTF-8',
    author = "Ronald Oussoren",
    author_email = "pyobjc-dev@lists.sourceforge.net",
    url = "https://bitbucket.org/ronaldoussoren/pyobjc",
    platforms = [ 'macOS' ],
    packages = [],
    install_requires = BASE_REQUIRES + framework_requires(),
    setup_requires = [],
    classifiers = CLASSIFIERS,
    license = 'MIT License',
    zip_safe = True,
    # workaround for setuptools 0.6b4 bug
    dependency_links = [],
    keywords=['Objective-C', 'bridge', 'Cocoa'],
    cmdclass={
        'test': oc_test,
	'egg_info': oc_egg_info,
    },
)
