#!/usr/bin/env python

import ez_setup
import sys

# ez_setup doesn't suppport the trunk of python (as well as ancient versions
# of python), check if a setuptools egg is listed for the current python version
# before going futher.

# We need at least Python 2.3
MIN_PYTHON = (2, 3)

if sys.version_info < MIN_PYTHON:
    vstr = '.'.join(map(str, MIN_PYTHON))
    raise SystemExit('PyObjC: Need at least Python ' + vstr)

v = "py%d.%d.egg"%(sys.version_info[:2])
for k in ez_setup.md5_data.keys():
    if k.endswith(v):
        break

else:
    try:
        import setuptools
    except ImportError:
        print "Ez_setup doesn't seem to support this version of python"
        print "Please install setuptools from source by hand. See "
        print "http://peak.telecommunity.com/DevCenter/setuptools for "
        print "more information on setuptools."
        sys.exit(1)


ez_setup.use_setuptools()

import sys
import os
import glob
import site

# If true we'll build universal binaries on systems with the 10.4u SDK running
# OS X 10.4 or later.
# 
# NOTE: This is an experimental feature.
AUTO_UNIVERSAL=0


# Add our dependencies to the path.
site.addsitedir(os.path.abspath('source-deps'))

# Add our utility library to the path
sys.path.insert(1,
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'setup-lib')))

OPTIONS = {'egg_info': {'egg_base': 'Lib'}}
from pyobjc_commands import extra_cmdclass, extra_options
OPTIONS.update(extra_options)

# Some PiPy stuff
LONG_DESCRIPTION="""
PyObjC is a bridge between Python and Objective-C.  It allows full
featured Cocoa applications to be written in pure Python.  It is also
easy to use other frameworks containing Objective-C class libraries
from Python and to mix in Objective-C, C and C++ source.

Python is a highly dynamic programming language with a shallow learning
curve.  It combines remarkable power with very clear syntax.

The installer package installs a number of Xcode templates for
easily creating new Cocoa-Python projects.

PyObjC also supports full introspection of Objective-C classes and
direct invocation of Objective-C APIs from the interactive interpreter.

PyObjC requires MacOS X 10.2 or later.  PyObjC works both with the Apple
provided Python installation in MacOS X 10.2 (and later) and with
MacPython 2.3.  Users of MacPython 2.3 can install PyObjC though the
PackageManager application.
"""

from setuptools import setup, Extension
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


    # Enable 'PyObjC_STRICT_DEBUGGING' to enable some costly internal 
    # assertions. 
    CFLAGS=[
        #"-DPyObjC_STRICT_DEBUGGING",
        "-DMACOSX",
        "-DAPPLE_RUNTIME",
        "-no-cpp-precomp",
        "-Wno-long-double",
        "-g",
        #"-O0",

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

    OBJC_LDFLAGS = frameworks('Foundation', 'Carbon')
    CF_LDFLAGS = frameworks('CoreFoundation', 'Foundation')
    FND_LDFLAGS = frameworks('CoreFoundation', 'Foundation')
    APPKIT_LDFLAGS = frameworks('CoreFoundation', 'AppKit')
    ADDRESSBOOK_LDFLAGS = frameworks('CoreFoundation', 'AddressBook', 'Foundation')
    SECURITY_INTERFACE_LDFLAGS = frameworks('CoreFoundation', 'SecurityInterface', 'Foundation')
    EXCEPTION_HANDLING_LDFLAGS = frameworks('CoreFoundation', 'ExceptionHandling', 'Foundation')
    PREFPANES_LDFLAGS = frameworks('CoreFoundation', 'PreferencePanes', 'Foundation')
    SENTESTINGKIT_LDFLAGS = frameworks('Foundation')

    BASE_LDFLAGS = []
    if AUTO_UNIVERSAL:
        if os.path.exists('/Developer/SDKs/MacOSX10.4u.sdk') and int(os.uname()[2].split('.')[0]) >= 8:
            CFLAGS.extend([
                    '-arch', 'i386',
                    '-arch', 'ppc',
                    '-isysroot', '/Developer/SDKs/MacOSX10.4u.sdk',
            ])
            BASE_LDFLAGS.extend([
                    '-arch', 'i386',
                    '-arch', 'ppc',
                    '-isysroot', '/Developer/SDKs/MacOSX10.4u.sdk',
                    #'-Wl,-syslibroot,/Developer/SDKs/MacOSX10.4u.sdk',
            ])


else:
    #
    # GNUstep
    #
    # NOTE: We add '-g' to the compile flags to make development easier
    # on systems where the installed python hasn't been build with debugging
    # support.
    gs_root = gs_root + '/Library'

    BASE_LDFLAGS=[]

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

FFI_CFLAGS=['-Ilibffi-src/include']

# The list below includes the source files for all CPU types that we run on
# this makes it easier to build fat binaries on Mac OS X.
FFI_SOURCE=[
    "libffi-src/src/types.c",
    "libffi-src/src/prep_cif.c",
    "libffi-src/src/x86/ffi_darwin.c",
    "libffi-src/src/x86/darwin.S",
    "libffi-src/src/powerpc/ffi_darwin.c",
    "libffi-src/src/powerpc/darwin.S",
    "libffi-src/src/powerpc/darwin_closure.S",
]

# Patch distutils: it needs to compile .S files as well.
from distutils.unixccompiler import UnixCCompiler
UnixCCompiler.src_extensions.append('.S')
del UnixCCompiler


CorePackages = [ 'objc' ]
objcExtension = Extension("objc._objc",
    FFI_SOURCE + list(glob.glob(os.path.join('Modules', 'objc', '*.m'))),
    extra_compile_args=CFLAGS + list(FFI_CFLAGS),
    extra_link_args=OBJC_LDFLAGS + BASE_LDFLAGS,
)

CoreExtensions =  [ objcExtension ]

for test_source in glob.glob(os.path.join('Modules', 'objc', 'test', '*.m')):
    name, ext = os.path.splitext(os.path.basename(test_source))

    if name != 'ctests':
        ext = Extension('objc.test.' + name,
            [test_source],
            extra_compile_args=['-IModules/objc'] + CFLAGS,
            extra_link_args=OBJC_LDFLAGS)
    else:
        ext = Extension('objc.test.' + name,
            [test_source] + FFI_SOURCE,
            extra_compile_args=['-IModules/objc'] + CFLAGS + FFI_CFLAGS,
            extra_link_args=OBJC_LDFLAGS + BASE_LDFLAGS)

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
AppleScriptKitDepends = dict(depends=INCFILES)
AutomatorDepends = dict(depends=INCFILES)
CoreDataDepends = dict(depends=INCFILES)
DiscRecordingDepends = dict(depends=INCFILES)
DiscRecordingUIDepends = dict(depends=INCFILES)
SyncServicesDepends = dict(depends=INCFILES)
XgridFoundationDepends = dict(depends=INCFILES)
QTKitDepends = dict(depends=INCFILES)
QuartzDepends = dict(depends=INCFILES)
OSAKitDepends = dict(depends=INCFILES)
SenTestingKitDepends = dict(depends=INCFILES)

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
                    ] + FND_LDFLAGS + BASE_LDFLAGS,
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
                    ] + APPKIT_LDFLAGS + BASE_LDFLAGS,
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
                      ] + ADDRESSBOOK_LDFLAGS + BASE_LDFLAGS,
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
                      ] + CF_LDFLAGS + BASE_LDFLAGS,
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
                      ] + SECURITY_INTERFACE_LDFLAGS + BASE_LDFLAGS,
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
                      ] + EXCEPTION_HANDLING_LDFLAGS + BASE_LDFLAGS,
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
                      ] + PREFPANES_LDFLAGS + BASE_LDFLAGS,
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

SenTestingKitPackages, SenTestingKitExtensions = \
        IfFrameWork('SenTestingKit.framework', [ 'SenTestingKit' ], [
            Extension('SenTestingKit._SenTestingKit',
                      [ 'Modules/SenTestingKit/_SenTestingKit.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=frameworks(
                        'SenTestingKit',
                        'Foundation'
                      ) + BASE_LDFLAGS,
                      **SenTestingKitDepends
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
                      ) + BASE_LDFLAGS,
                      **WebKitDepends
                      ),
        ], headername="WebKit.h")

XgridFoundationPackages, XgridFoundationExtensions = \
        IfFrameWork('XgridFoundation.framework', [ 'XgridFoundation' ], [
            Extension('XgridFoundation._XgridFoundation',
                      [ 'Modules/XgridFoundation/_XgridFoundation.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=frameworks(
                        'XgridFoundation',
                        'Foundation'
                      ) + BASE_LDFLAGS,
                      **XgridFoundationDepends
                      ),
        ], headername="XgridFoundation.h")

CoreDataPackages, CoreDataExtensions = \
        IfFrameWork('CoreData.framework', [ 'CoreData' ], [
            Extension('CoreData._CoreData',
                      [ 'Modules/CoreData/_CoreData.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=frameworks(
                        'CoreData',
                        'Foundation'
                      ) + BASE_LDFLAGS,
                      **CoreDataDepends
                      ),
        ], headername="CoreData.h")

DiscRecordingPackages, DiscRecordingExtensions = \
        IfFrameWork('DiscRecording.framework', [ 'DiscRecording' ], [
            Extension('DiscRecording._DiscRecording',
                      [ 'Modules/DiscRecording/_DiscRecording.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=frameworks(
                        'DiscRecording',
                        'Foundation'
                      ) + BASE_LDFLAGS,
                      **DiscRecordingDepends
                      ),
        ], headername="DiscRecording.h")

DiscRecordingUIPackages, DiscRecordingUIExtensions = \
        IfFrameWork('DiscRecordingUI.framework', [ 'DiscRecordingUI' ], [
            Extension('DiscRecordingUI._DiscRecordingUI',
                      [ 'Modules/DiscRecordingUI/_DiscRecordingUI.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=frameworks(
                        'DiscRecordingUI',
                        'Foundation'
                      ) + BASE_LDFLAGS,
                      **DiscRecordingUIDepends
                      ),
        ], headername="DiscRecordingUI.h")

SyncServicesPackages, SyncServicesExtensions = \
        IfFrameWork('SyncServices.framework', [ 'SyncServices' ], [
            Extension('SyncServices._SyncServices',
                      [ 'Modules/SyncServices/_SyncServices.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=frameworks(
                        'SyncServices',
                        'Foundation'
                      ) + BASE_LDFLAGS,
                      **SyncServicesDepends
                      ),
        ], headername="SyncServices.h")

AutomatorPackages, AutomatorExtensions = \
        IfFrameWork('Automator.framework', [ 'Automator' ], [
            Extension('Automator._Automator',
                      [ 'Modules/Automator/_Automator.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=frameworks(
                        'Automator',
                        'Foundation'
                      ) + BASE_LDFLAGS,
                      **AutomatorDepends
                      ),
        ], headername="Automator.h")

QTKitPackages, QTKitExtensions = \
        IfFrameWork('QTKit.framework', [ 'QTKit' ], [
            Extension('QTKit._QTKit',
                      [ 'Modules/QTKit/_QTKit.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=frameworks(
                        'QTKit',
                        'Foundation'
                      ) + BASE_LDFLAGS,
                      **QTKitDepends
                      ),
        ], headername="QTKit.h")

QuartzPackages, QuartzExtensions = \
        IfFrameWork('Quartz.framework', [ 'Quartz' ], [
            Extension('Quartz._Quartz',
                      [ 'Modules/Quartz/_Quartz.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=frameworks(
                        'Quartz',
                        'Foundation'
                      ) + BASE_LDFLAGS,
                      **QuartzDepends
                      ),
        ], headername="Quartz.h")

OSAKitPackages, OSAKitExtensions = \
        IfFrameWork('OSAKit.framework', [ 'OSAKit' ], [
            Extension('OSAKit._OSAKit',
                      [ 'Modules/OSAKit/_OSAKit.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=frameworks(
                        'OSAKit',
                        'Foundation'
                      ) + BASE_LDFLAGS,
                      **OSAKitDepends
                      ),
        ], headername="OSAKit.h")

AppleScriptKitPackages, AppleScriptKitExtensions = \
        IfFrameWork('AppleScriptKit.framework', [ 'AppleScriptKit' ], [
            Extension('AppleScriptKit._AppleScriptKit',
                      [ 'Modules/AppleScriptKit/_AppleScriptKit.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=frameworks(
                        'AppleScriptKit',
                        'Foundation'
                      ) + BASE_LDFLAGS,
                      **AppleScriptKitDepends
                      ),
        ], headername="ASKPluginObject.h")



def package_version():
    fp = open('Modules/objc/pyobjc.h', 'r')
    for ln in fp.readlines():
        if ln.startswith('#define OBJC_VERSION'):
            fp.close()
            return ln.split()[-1][1:-1]

    raise ValueError, "Version not found"


# skipping CoreFoundationPackages, it's fake!
packages = (
    CorePackages +
    AppKitPackages +
    FoundationPackages +
    AddressBookPackages +
    PrefPanesPackages +
    InterfaceBuilderPackages +
    ScreenSaverPackages +
    WebKitPackages +
    MessagePackages +
    SecurityInterfacePackages +
    ExceptionHandlingPackages +
    # Mac OS X 10.4
    AppleScriptKitPackages +
    AutomatorPackages +
    CoreDataPackages +
    DiscRecordingPackages +
    DiscRecordingUIPackages +
    SyncServicesPackages +
    XgridFoundationPackages +
    QTKitPackages +
    QuartzPackages +
    OSAKitPackages +
    SenTestingKitPackages +

    [
        'PyObjCTools',
        'PyObjCTools.XcodeSupport',
    ]
)

# The following line is needed to allow separate flat modules
# to be installed from a different folder
package_dir = dict([(pkg, 'Lib/' + pkg.replace('.', '/')) for pkg in packages])

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

if gs_root is not None:
    install_requires = setup_requires = []
else:
    install_requires = setup_requires = ['py2app>=0.3.1', 'bdist_mpkg>=0.4.2']

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
       # Mac OS X 10.4
       + AppleScriptKitExtensions
       + AutomatorExtensions
       + QTKitExtensions
       + QuartzExtensions
       + OSAKitExtensions
       + CoreDataExtensions
       + DiscRecordingExtensions
       + DiscRecordingUIExtensions
       + SyncServicesExtensions
       + XgridFoundationExtensions
       + SenTestingKitExtensions

    ),
    packages = packages,
    package_dir = package_dir,
    install_requires = install_requires,
    setup_requires = setup_requires,
    entry_points = {
        'console_scripts': [
            "nibclassbuilder = PyObjCTools.NibClassBuilder:commandline"
        ],
    },
    extra_path = "PyObjC",
    cmdclass = extra_cmdclass,
    options = OPTIONS,
    classifiers = CLASSIFIERS,
    license = 'MIT License',
    download_url = 'http://pyobjc.sourceforge.net/software/index.php',
    zip_safe = False,
    # workaround for setuptools 0.6b4 bug
    dependency_links = [],
)

if 'install' in sys.argv:
    import textwrap
    print textwrap.dedent(
    """
    **NOTE**

    Installing PyObjC with "setup.py install" *does not* install the following:
    
    - py2app (bdist_mpkg, modulegraph, altgraph, ...) and its tools
    - Xcode templates
    - Documentation
    - Example code

    The recommended method for installing PyObjC is to do:
        
        $ python setup.py bdist_mpkg --open

    This will create and open an Installer metapackage that contains PyObjC,
    py2app, and all the goodies!
    """)
