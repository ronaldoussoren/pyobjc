#!/usr/bin/env python

import sys
import os
import glob
import site

# We need at least Python 2.3
MIN_PYTHON = (2, 3)

if sys.version_info < MIN_PYTHON:
    vstr = '.'.join(map(str, MIN_PYTHON))
    raise SystemExit('PyObjC: Need at least Python ' + vstr)

# Add our utility library to the path
site.addsitedir(os.path.abspath('source-deps'))
sys.path.insert(1,
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'setup-lib')))

from pyobjc_commands import extra_cmdclass

# Some PiPy stuff
LONG_DESCRIPTION="""
PyObjC is a bridge between Python and Objective-C.  It allows full
featured Cocoa applications to be written in pure Python.  It is also
easy to use other frameworks containing Objective-C class libraries
from Python and to mix in Objective-C, C and C++ source.

Python is a highly dynamic programming language with a shallow learning
curve.  It combines remarkable power with very clear syntax.

The installer package installs a number of Project Builder templates for
easily creating new Cocoa-Python projects, as well as support for syntax
coloring of Python files in Project Builder.

PyObjC also supports full introspection of Objective-C classes and
direct invocation of Objective-C APIs from the interactive interpreter.

PyObjC requires MacOS X 10.2 or later.  PyObjC works both with the Apple
provided Python installation in MacOS X 10.2 (and later) and with
MacPython 2.3.  Users of MacPython 2.3 can install PyObjC though the
PackageManager application.
"""

from distutils.core import setup, Extension
import os

def frameworks(*args):
    lst = []
    for arg in args:
        lst.extend(['-framework', arg])
    return lst

# On GNUstep we can read some configuration from the environment.
gs_root = os.environ.get('GNUSTEP_SYSTEM_ROOT')

if gs_root is None:
    #
    # MacOS X
    #
    def IfFrameWork(name, packages, extensions, headername=None):
        """
        Return the packages and extensions if the framework exists, or
        two empty lists if not.
        """
        for pth in ('/System/Library/Frameworks', '/Library/Frameworks'):
            basedir = os.path.join(pth, name)
            if os.path.exists(basedir):
                if (headername is None) or os.path.exists(os.path.join(basedir, "Headers", headername)):
                    return packages, extensions
        return [], []

    # Double-check
    if sys.platform != 'darwin':
        print "You're not running on MacOS X, and don't use GNUstep"
        print "I don't know how to build PyObjC on such a platform."
        print "Please read the ReadMe."
        print ""
        raise SystemExit("ObjC runtime not found")

    CFLAGS=[
        "-DMACOSX",
        "-DAPPLE_RUNTIME",
        "-no-cpp-precomp",
        "-Wno-long-double",
        "-g",
        "-O0",

        # Loads of warning flags
        "-Wall", "-Wstrict-prototypes", "-Wmissing-prototypes",
        "-Wformat=2", "-W", "-Wshadow",
        "-Wpointer-arith", #"-Wwrite-strings",
        "-Wmissing-declarations",
        "-Wnested-externs",
        "-Wno-long-long",
        #"-Wfloat-equal",

        # These two are fairly useless:
        #"-Wunreachable-code",
        #"-pedantic",

        "-Wno-import",
        #"-Werror",

        # use the same optimization as Python, probably -O3,
        # but can be overrided by one of the following:

        # no optimization, for debugging
        #"-O0",

        # g4 optimized
        #"-fast", "-fPIC", "-mcpu=7450",

        # g5 optimized
        #"-fast", "-fPIC",
        ]

    OBJC_LDFLAGS = frameworks('Foundation')
    CF_LDFLAGS = frameworks('CoreFoundation', 'Foundation')
    FND_LDFLAGS = frameworks('CoreFoundation', 'Foundation')
    APPKIT_LDFLAGS = frameworks('CoreFoundation', 'AppKit')
    ADDRESSBOOK_LDFLAGS = frameworks('CoreFoundation', 'AddressBook', 'Foundation')
    SECURITY_INTERFACE_LDFLAGS = frameworks('CoreFoundation', 'SecurityInterface', 'Foundation')
    EXCEPTION_HANDLING_LDFLAGS = frameworks('CoreFoundation', 'ExceptionHandling', 'Foundation')
    PREFPANES_LDFLAGS = frameworks('CoreFoundation', 'PreferencePanes', 'Foundation')

else:
    #
    # GNUstep
    #
    # NOTE: We add '-g' to the compile flags to make development easier
    # on systems where the installed python hasn't been build with debugging
    # support.
    gs_root = gs_root + '/Library'

    gs_cpu = os.environ.get('GNUSTEP_HOST_CPU')
    gs_os = os.environ.get('GNUSTEP_HOST_OS')
    gs_combo = os.environ.get('LIBRARY_COMBO')

    gs_lib_dir = gs_cpu + '/' + gs_os
    gs_flib_dir = gs_cpu + '/' + gs_os + '/' + gs_combo

    def IfFrameWork(name, packages, extensions, headername=None):
        """
        Return the packages and extensions if the framework exists, or
        two empty lists if not.
        """
        name = os.path.splitext(name)[0]
        for pth in (gs_root, ):
            basedir = os.path.join(pth, 'Headers', name)
            if os.path.exists(basedir):
                return packages, extensions
        return [], []

    CFLAGS=[
        '-g',
        ##'-O0',
        '-Wno-import',

        # The flags below should somehow be extracted from the GNUstep
        # build environment (makefiles)!
        '-DGNU_RUNTIME=1',
        '-DGNUSTEP_BASE_LIBRARY=1',
        '-fconstant-string-class=NSConstantString',
        '-fgnu-runtime',
        '-I' + gs_root + '/Headers',
        '-I' + gs_root + '/Headers/gnustep',
        '-I' + gs_root + '/Headers/' + gs_lib_dir
        ]

    OBJC_LDFLAGS=[
        '-g',
        '-L', gs_root + '/Libraries/',
        '-L', gs_root + '/Libraries/' + gs_flib_dir,
        '-L', gs_root + '/Libraries/' + gs_lib_dir,
        '-lgnustep-base',
        '-lobjc'
        ]

    FND_LDFLAGS = OBJC_LDFLAGS
    FNDMAP_LDFLAGS = OBJC_LDFLAGS
    APPKIT_LDFLAGS = OBJC_LDFLAGS + ['-lgnustep-gui']
    APPMAP_LDFLAGS = OBJC_LDFLAGS + ['-lgnustep-gui']
    CF_LDFLAGS = []
    ADDRESSBOOK_LDFLAGS = OBJC_LDFLAGS + ['-lAddresses']
    PREFPANES_LDFLAGS = []
    SECURITY_INTERFACE_LDFLAGS = []
    EXCEPTION_HANDLING_LDFLAGS = []

CFLAGS.append('-Ibuild/codegen/')

CorePackages = [ 'objc' ]
objcExtension = Extension("objc._objc",
    glob.glob(os.path.join('Modules', 'objc', '*.m')),
    extra_compile_args=CFLAGS,
    extra_link_args=OBJC_LDFLAGS,
)
objcExtension.use_libffi = True

CoreExtensions =  [ objcExtension ]

for test_source in glob.glob(os.path.join('Modules', 'objc', 'test', '*.m')):
    name, ext = os.path.splitext(os.path.basename(test_source))
    ext = Extension('objc.test.' + name,
        [test_source],
        extra_compile_args=['-IModules/objc'] + CFLAGS,
        extra_link_args=OBJC_LDFLAGS)
    if name == 'ctests':
        ext.use_libffi = True
    CoreExtensions.append(ext)

CoreFoundationDepends = dict()

FoundationDepends = dict(
    depends=(
          glob.glob('build/codegen/_Fnd_*.inc')
        + glob.glob('Modules/Foundation/*.m')
    ),
)

AppKitDepends = dict(
    depends=(
          glob.glob('build/codegen/_App_*.inc')
        + glob.glob('Modules/AppKit/*.m')
    ),
)

INCFILES = glob.glob('build/codegen/*.inc')

AddressBookDepends = dict(depends=INCFILES)
SecurityInterfaceDepends = dict(depends=INCFILES)
ExceptionHandlingDepends = dict(depends=INCFILES)
PrefPanesDepends = dict(depends=INCFILES)
InterfaceBuilderDepends = dict(depends=INCFILES)
WebKitDepends = dict(depends=INCFILES)

FoundationPackages, FoundationExtensions = \
        IfFrameWork('Foundation.framework', [ 'Foundation' ], [
          Extension("Foundation._Foundation",
                    [
                        "Modules/Foundation/_Foundation.m",
                    ],
                    extra_compile_args=[
                        "-IModules/objc",
                    ] + CFLAGS,
                    extra_link_args=[
                    ] + FND_LDFLAGS,
                    **FoundationDepends
                    ),
        ])

AppKitPackages, AppKitExtensions = \
        IfFrameWork('AppKit.framework', [ 'AppKit' ], [
          Extension("AppKit._AppKit",
                    ["Modules/AppKit/_AppKit.m"],
                    extra_compile_args=[
                        "-IModules/objc",
                    ] + CFLAGS,
                    extra_link_args=[
                    ] + APPKIT_LDFLAGS,
                    **AppKitDepends
                    ),
      ])

# The AdressBook module is only installed when the user actually has the
# AddressBook framework.
AddressBookPackages, AddressBookExtensions = \
        IfFrameWork('AddressBook.framework', [ 'AddressBook' ], [
            Extension('AddressBook._AddressBook',
                      [ 'Modules/AddressBook/_AddressBook.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=[
                      ] + ADDRESSBOOK_LDFLAGS,
                      **AddressBookDepends
                      ),
        ])

CoreFoundationPackages, CoreFoundationExtensions = \
        IfFrameWork('CoreFoundation.framework', [ 'CoreFoundation' ], [
            Extension("PyObjCTools._machsignals",
                      [ 'Modules/CoreFoundation/machsignals.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=[
                      ] + CF_LDFLAGS,
                      **CoreFoundationDepends),
        ])

SecurityInterfacePackages, SecurityInterfaceExtensions = \
        IfFrameWork('SecurityInterface.framework', [ 'SecurityInterface' ], [
            Extension('SecurityInterface._SecurityInterface',
                      [ 'Modules/SecurityInterface/_SecurityInterface.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=[
                      ] + SECURITY_INTERFACE_LDFLAGS,
                      **SecurityInterfaceDepends
                      ),
        ])

ExceptionHandlingPackages, ExceptionHandlingExtensions = \
        IfFrameWork('ExceptionHandling.framework', [ 'ExceptionHandling' ], [
            Extension('ExceptionHandling._ExceptionHandling',
                      [ 'Modules/ExceptionHandling/_ExceptionHandling.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=[
                      ] + EXCEPTION_HANDLING_LDFLAGS,
                      **ExceptionHandlingDepends
                      ),
        ])

PrefPanesPackages, PrefPanesExtensions = \
        IfFrameWork('PreferencePanes.framework', [ 'PreferencePanes' ], [
            Extension('PreferencePanes._PreferencePanes',
                      [ 'Modules/PreferencePanes/_PreferencePanes.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=[
                      ] + PREFPANES_LDFLAGS,
                      **PrefPanesDepends
                      ),
        ])

ScreenSaverPackages, ScreenSaverExtensions = \
        IfFrameWork('ScreenSaver.framework', [ 'ScreenSaver' ], [])
        
MessagePackages, MessageExtensions = \
        IfFrameWork('Message.framework', [ 'Message' ], [])

InterfaceBuilderPackages, InterfaceBuilderExtensions = \
        IfFrameWork('InterfaceBuilder.framework', [ 'InterfaceBuilder' ], [
            Extension('InterfaceBuilder._InterfaceBuilder',
                      [ 'Modules/InterfaceBuilder/_InterfaceBuilder.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=frameworks(
                        'InterfaceBuilder',
                        'Foundation'
                      ),
                      **InterfaceBuilderDepends
                      ),
        ])

WebKitPackages, WebKitExtensions = \
        IfFrameWork('WebKit.framework', [ 'WebKit' ], [
            Extension('WebKit._WebKit',
                      [ 'Modules/WebKit/_WebKit.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=frameworks(
                        'WebKit',
                        'Foundation'
                      ),
                      **WebKitDepends
                      ),
        ], headername="WebKit.h")


def package_version():
    fp = open('Modules/objc/pyobjc.h', 'r')
    for ln in fp.readlines():
        if ln.startswith('#define OBJC_VERSION'):
            fp.close()
            return ln.split()[-1][1:-1]

    raise ValueError, "Version not found"


# skipping CoreFoundationPackages, it's fake!
packages = (
      CorePackages
    + AppKitPackages
    + FoundationPackages
    + AddressBookPackages
    + PrefPanesPackages
    + InterfaceBuilderPackages
    + ScreenSaverPackages
    + WebKitPackages
    + MessagePackages
    + SecurityInterfacePackages
    + ExceptionHandlingPackages
    + [ 'PyObjCTools' , 'PyObjCScripts' ]
)

# The following line is needed to allow separate flat modules
# to be installed from a different folder
package_dir = dict([(pkg, 'Lib/' + pkg) for pkg in packages])

for aPackage in package_dir.keys():
    testDir = os.path.join(package_dir[aPackage], 'test')
    if os.path.isdir(testDir):
        packageName = '%s.test' % aPackage
        package_dir[packageName] = testDir
        packages.append(packageName)

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
    version = package_version(),
    description = "Python<->ObjC Interoperability Module",
    long_description = LONG_DESCRIPTION,
    author = "bbum, RonaldO, SteveM, LeleG, many others stretching back through the reaches of time...",
    author_email = "pyobjc-dev@lists.sourceforge.net",
    url = "http://pyobjc.sourceforge.net/",
    platforms = [ 'MacOS X' ],
    ext_modules = (
         CoreExtensions
       + AppKitExtensions
       + FoundationExtensions
       + AddressBookExtensions
       + PrefPanesExtensions
       + InterfaceBuilderExtensions
       + ScreenSaverExtensions
       + MessageExtensions
       + SecurityInterfaceExtensions
       + ExceptionHandlingExtensions
       + CoreFoundationExtensions
       + WebKitExtensions
    ),
    packages = packages,
    package_dir = package_dir,
    scripts = [ 'Scripts/nibclassbuilder', ],
    extra_path = "PyObjC",
    cmdclass = extra_cmdclass,
    classifiers = CLASSIFIERS,
    license = 'MIT License',
    download_url = 'http://pyobjc.sourceforge.net/software/index.php',
)

if 'install' in sys.argv:
    import textwrap
    print textwrap.dedent(
    """
    **NOTE**

    Installing PyObjC with "setup.py install" *does not* install the following:
    
    - py2app (bdist_mpkg, modulegraph, altgraph, ...) and its tools
    - Xcode or Project Builder templates
    - Documentation
    - Example code

    The recommended method for installing PyObjC is to do:
        
        $ python setup.py bdist_mpkg --open

    This will create and open an Installer metapackage that contains PyObjC,
    py2app, and all the goodies!
    """)
