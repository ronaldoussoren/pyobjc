#!/usr/bin/env python

# Set this to the path to an extracted tree of libffi to automaticly build
# a compatible version of libffi
LIBFFI_SOURCES=None
LIBFFI_SOURCES='libffi-src'

import sys
import os
import glob

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

if sys.version >= '2.2.3':
    SetupExtraArguments = {
        'classifiers': [
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Environment :: MacOS X :: Cocoa',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Operating System :: MacOS :: MacOS X',
            'Programming Language :: Python',
            'Programming Language :: Objective C',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: User Interfaces',
        ],
        'download_url': 'http://pyobjc.sourceforge.net/software/index.php',
    }
else:
    SetupExtraArguments = {}

if sys.platform == 'darwin': 
    # Apple has used build options that don't work with a 'normal' system.
    # Remove '-arch i386' from the LDFLAGS.
    import distutils.sysconfig
    distutils.sysconfig.get_config_vars()
    x = distutils.sysconfig._config_vars['LDSHARED']
    y = x.replace('-arch i386', '')
    if y != x:
        print "Fixing Apple strangeness in Python configuration"
        distutils.sysconfig._config_vars['LDSHARED'] = y

from distutils.core import setup, Extension
import os

def subprocess(taskName, cmd, validRes=None):
    print "Performing task: %s" % (taskName,)
    fd = os.popen(cmd, 'r')
    for ln in fd.xreadlines():
        sys.stdout.write(ln)

    res = fd.close()
    if res is not validRes:
        sys.stderr.write("Task '%s' failed [%d]\n"%(taskName, res))
        sys.exit(1)

# We need at least Python 2.2
req_ver = [ 2, 2]

if sys.version_info[0] < req_ver[0] or (
        sys.version_info[0] == req_ver[0] 
        and sys.version_info[1] < req_ver[1]):

    sys.stderr.write('PyObjC: Need at least Python %s\n'%('.'.join(req_ver)))
    sys.exit(1)

if LIBFFI_SOURCES is not None:
    if not os.path.isdir(LIBFFI_SOURCES):
        sys.stderr.write(
            'LIBFFI_SOURCES is not a directory: %s\n'%LIBFFI_SOURCES)
        sys.stderr.write('\tSee Install.txt or Install.html for more information.\n')
        sys.exit(1)
    
    if not os.path.exists('build'):
        os.mkdir('build')

    if not os.path.exists('build/libffi'):
        os.mkdir('build/libffi')

    if not os.path.exists('build/libffi/BLD'):
        os.mkdir('build/libffi/BLD')

    if not os.path.exists('build/libffi/lib/libffi.a'):
        # No pre-build version available, build it now.
        # Do not use a relative path for the build-tree, libtool on
        # MacOS X doesn't like that.
        inst_dir = os.path.join(os.getcwd(), 'build/libffi')
        src_path = os.path.abspath(LIBFFI_SOURCES)

        inst_dir = inst_dir.replace("'", "'\"'\"'")
        src_path = src_path.replace("'", "'\"'\"'")

        subprocess('Building FFI', "cd build/libffi/BLD && '%s/configure' --prefix='%s' --disable-shared --enable-static && make install"%(src_path, inst_dir), None)
        
    LIBFFI_BASE='build/libffi'

elif os.environ.has_key('LIBFFI_BASE'):
    LIBFFI_BASE=os.environ['LIBFFI_BASE']
else:
    LIBFFI_BASE='libffi'
LIBFFI_CFLAGS=[ 
    "-isystem", "%s/include"%LIBFFI_BASE, 
]
LIBFFI_LDFLAGS=[ 
    '-L%s/lib'%LIBFFI_BASE, '-lffi', 
]

sourceFiles = [
        "Modules/objc/objc_util.m",
        "Modules/objc/objc_support.m",
        "Modules/objc/class-builder.m",
        "Modules/objc/class-list.m",
        "Modules/objc/ObjCPointer.m",
        "Modules/objc/py2.2bool.c",
        "Modules/objc/objc-class.m",
        "Modules/objc/unicode-object.m",
        "Modules/objc/informal-protocol.m",
        "Modules/objc/objc-object.m",
        "Modules/objc/super-call.m",
        "Modules/objc/selector.m",
        "Modules/objc/method-accessor.m",
        "Modules/objc/instance-var.m",
        "Modules/objc/OC_PythonObject.m",
        "Modules/objc/OC_PythonArray.m",
        "Modules/objc/OC_PythonDictionary.m",
        "Modules/objc/pyobjc-api.m",
        "Modules/objc/alloc_hack.m",
        "Modules/objc/toll-free-bridging.m",
        "Modules/objc/module.m",
        "Modules/objc/libffi_support.m",
        "Modules/objc/pointer-support.m",
]

# On GNUstep we can read some configuration from the environment.
gs_root = os.environ.get('GNUSTEP_SYSTEM_ROOT')

if gs_root is None:
    #
    # MacOS X 
    #
    CFLAGS=[
        "-DMACOSX",
        "-no-cpp-precomp",
        "-Wno-long-double",
        "-g",

        # Loads of warning flags
        "-Wall", "-Wstrict-prototypes", "-Wmissing-prototypes",
        "-Wformat=2", "-W", "-Wfloat-equal", "-Wshadow", 
        "-Wpointer-arith", #"-Wwrite-strings",
        "-Wmissing-declarations",
        "-Wnested-externs", 
        "-Wno-long-long",
    
        # These two are fairly useless:
        #"-Wunreachable-code", 
        #"-pedantic",

        "-Wno-import", 
        #"-O0", "-g",
        #"-Werror",
        ]

    OBJC_LDFLAGS=[
        '-framework', 'Foundation',
        ]

    FND_LDFLAGS=[
        '-framework CoreFoundation', '-framework', 'Foundation',
        ]

    APPKIT_LDFLAGS=[
        '-framework CoreFoundation', '-framework', 'AppKit',
        ]

    FNDMAP_LDFLAGS=[
        '-framework CoreFoundation', '-framework', 'Foundation',
        ]

    APPMAP_LDFLAGS=[
        '-framework CoreFoundation', '-framework', 'AppKit',
        ]

    ADDRESSBOOK_LDFLAGS=[
        '-framework CoreFoundation', '-framework', 'AddressBook', '-framework', 'Foundation',
    ]

    PREFPANES_LDFLAGS=[
        '-framework CoreFoundation', '-framework', 'PreferencePanes', '-framework', 'Foundation',
    ]

else:
    #
    # GNUstep
    #
    # NOTE: We add '-g' to the compile flags to make development easier
    # on systems where the installed python hasn't been build with debugging
    # support.

    gs_cpu = os.environ.get('GNUSTEP_HOST_CPU')
    gs_os = os.environ.get('GNUSTEP_HOST_OS')
    gs_combo = os.environ.get('LIBRARY_COMBO')

    gs_lib_dir = gs_cpu + '/' + gs_os
    gs_flib_dir = gs_cpu + '/' + gs_os + '/' + gs_combo

    CFLAGS=[
        '-g',
        '-Wno-import',
        '-DGNU_RUNTIME',
        '-DGNUSTEP',
        '-I' + gs_root + '/Headers',
        '-I' + gs_root + '/Headers/gnustep',
        '-I' + gs_root + '/Headers/' + gs_lib_dir
        ]

    OBJC_LDFLAGS=[
        '-g',
        '-L', gs_root + '/Libraries/' + gs_flib_dir,
        '-l', 'gnustep-base',
        '-L', gs_root + '/Libraries/' + gs_lib_dir,
        '-l', 'objc'
        ]

    FND_LDFLAGS=[
        '-g',
        '-L', gs_root + '/Libraries/' + gs_flib_dir,
        '-l', 'gnustep-base',
        '-L', gs_root + '/Libraries/' + gs_lib_dir,
        '-l', 'objc'
        ]

    APPKIT_LDFLAGS=[
        '-g',
        '-L', gs_root + '/Libraries/' + gs_flib_dir,
        '-l', 'gnustep-base',
        '-l', 'gnustep-gui',
        '-L', gs_root + '/Libraries/' + gs_lib_dir,
        '-l', 'objc'
        ]

    FNDMAP_LDFLAGS=[
        '-g',
        '-L', gs_root + '/Libraries/' + gs_flib_dir,
        '-l', 'gnustep-base',
        '-L', gs_root + '/Libraries/' + gs_lib_dir,
        '-l', 'objc'
        ]

    APPMAP_LDFLAGS=[
        '-g',
        '-L', gs_root + '/Libraries/' + gs_flib_dir,
        '-l', 'gnustep-base',
        '-l', 'gnustep-gui',
        '-L', gs_root + '/Libraries/' + gs_lib_dir,
        '-l', 'objc'
        ]

    ADDRESSBOOK_LDFLAGS=[]
    PREFPANES_LDFLAGS=[]

CFLAGS.append('-IInclude/')
CFLAGS.append('-Ibuild/codegen/')

def IfFrameWork(name, packages, extensions):
    """
    Return the packages and extensions if the framework exists, or
    two empty lists if not.
    """
    if os.path.exists(os.path.join('/System/Library/Frameworks/', name)):
        return packages, extensions
    if os.path.exists(os.path.join('/Library/Frameworks/', name)):
        return packages, extensions
    return [], []



CorePackages = [ 'objc' ]
CoreExtensions =  [
    Extension("objc._objc", 
              sourceFiles,
              extra_compile_args=[
              ] + LIBFFI_CFLAGS + CFLAGS,
              extra_link_args=LIBFFI_LDFLAGS + OBJC_LDFLAGS),
    Extension("objc.test.testbndl",
              ["Lib/objc/test/testbndl.m"],
              extra_compile_args=["-IModules/objc" ] + CFLAGS,
              extra_link_args=OBJC_LDFLAGS),
    Extension("objc.test.testbndl2",
              ["Lib/objc/test/testbndl2.m"],
              extra_compile_args=["-IModules/objc" ] + CFLAGS,
              extra_link_args=OBJC_LDFLAGS),
    Extension("autoGIL", 
              ["Modules/autoGIL.c"],
              extra_compile_args = CFLAGS,
              extra_link_args = ['-framework', 'CoreFoundation']),
    ]
CocoaPackages = [ 'Foundation', 'AppKit' ]

# XXX: Should not do this every time setup.py is called!
subprocess("Generating wrappers & stubs", "%s Scripts/CodeGenerators/cocoa_generator.py" % (sys.executable,), None)

# Provide some dependency information on Python 2.3 and later, this
# makes development slightly more convenient.
if sys.version >= '2.3':
    FoundationDepends = {
        'depends': glob.glob('Modules/Foundation/_Fnd_*.inc'),
    }
    AppKitDepends = {
        'depends': glob.glob('Modules/AppKit/_App_*.inc'),
    }
    AppKitMappingDepends = {
        'depends': glob.glob('Modules/AppKit/_AppKitMapping_*.m'),
    }
    FoundationMappingDepends = {
        'depends': glob.glob('Modules/Foundation/_FoundationMapping_*.m'),
    }
    AddressBookDepends = {
        'depends': glob.glob('Modules/AddressBook/*.inc'),
    }
    PrefPanesDepends = {
        'depends': glob.glob('Modules/PreferencePanes/*.inc'),
    }
    InterfaceBuilderDepends = {
        'depends': glob.glob('Modules/InterfaceBuilder/*.inc'),
    }
    WebKitDepends = {
        'depends': glob.glob('Modules/WebKit/*.inc'),
    }
else:
    FoundationDepends = {}
    AppKitDepends = {}
    AppKitMappingDepends = {}
    FoundationMappingDepends = {}
    AddressBookDepends = {}
    PrefPanesDepends = {}
    InterfaceBuilderDepends = {}
    WebKitDepends = {}

CocoaExtensions = [
          Extension("Foundation._Foundation", 
                    [
                        "Modules/Foundation/_Foundation.m",
                        "Modules/Foundation/NSAutoreleasePoolSupport.m"
                    ],
                    extra_compile_args=[
                        "-IModules/objc",  
                    ] + CFLAGS,
                    extra_link_args=[
                    ] + FND_LDFLAGS,
                    **FoundationDepends
                    ),
          Extension("AppKit._AppKit", 
                    ["Modules/AppKit/_AppKit.m"],
                    extra_compile_args=[
                        "-IModules/objc", 
                    ] + CFLAGS,
                    extra_link_args=[
                    ] + APPKIT_LDFLAGS,
                    **AppKitDepends
                    ),
          Extension("AppKit._AppKitMapping",
                    ["Modules/AppKit/_AppKitMapping.m"],
                    extra_compile_args=[ "-IModules/objc",] + CFLAGS,
                    extra_link_args=[] + APPMAP_LDFLAGS,
                    **AppKitMappingDepends
                    ),
          Extension("objc._FoundationMapping", 
                    ["Modules/Foundation/_FoundationMapping.m"],
                    extra_compile_args=[
                        "-IModules/objc", 
                    ] + CFLAGS,
                    extra_link_args=[
                    ] + FNDMAP_LDFLAGS,
                    **FoundationMappingDepends
                    ),
      ]

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

InterfaceBuilderPackages, InterfaceBuilderExtensions = \
        IfFrameWork('InterfaceBuilder.framework', [ 'InterfaceBuilder' ], [
            Extension('InterfaceBuilder._InterfaceBuilder',
                      [ 'Modules/InterfaceBuilder/_InterfaceBuilder.m' ],
                      extra_compile_args=[
                        '-IModules/objc',
                      ] + CFLAGS,
                      extra_link_args=[
                        '-framework', 'InterfaceBuilder', 
                        '-framework', 'Foundation'
                      ],
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
                      extra_link_args=[
                        '-framework', 'WebKit', 
                        '-framework', 'Foundation'
                      ],
                      **WebKitDepends
                      ),
        ])


def package_version():
    fp = open('Modules/objc/pyobjc.h', 'r')
    for ln in fp.readlines():
        if ln.startswith('#define OBJC_VERSION'):
            fp.close()
            return ln.split()[-1][1:-1]

    raise ValueError, "Version not found"


packages = CorePackages + CocoaPackages + AddressBookPackages + PrefPanesPackages + InterfaceBuilderPackages + ScreenSaverPackages + WebKitPackages + [ 'PyObjCTools' ] 
# The following line is needed to allow separate flat modules
# to be installed from a different folder (needed for the 
# bundlebuilder test below).
package_dir = dict([(pkg, 'Lib/' + pkg) for pkg in packages])

for aPackage in package_dir.keys():
    testDir = os.path.join(package_dir[aPackage], 'test')
    if os.path.isdir(testDir):
        packageName = '%s.test' % aPackage
        package_dir[packageName] = testDir
        packages.append(packageName)

try:
    import bundlebuilder

    if sys.version_info[:2] == (2,2):
        raise ImportError, "We're the only provider of these modules ATM."
except ImportError:
    # bundlebuilder.py and plistlib.py shipped with newer versions of
    # Python but are included with pyobjc be independent. The following
    # magic makes distutils install the contents of MPCompat.
    packages.append('')
    package_dir[''] = 'MPCompat'

dist = setup(name = "pyobjc",
	     version = package_version(),
	     description = "Python<->ObjC Interoperability Module",
             long_description = LONG_DESCRIPTION,
	     author = "bbum, RonaldO, SteveM, LeleG, many others stretching back through the reaches of time...",
	     author_email = "pyobjc-dev@lists.sourceforge.net",
	     url = "http://pyobjc.sourceforge.net/",
             platforms = [ 'MacOS X' ],
	     ext_modules = (
			     CoreExtensions 
			   + CocoaExtensions 
			   + AddressBookExtensions 
                           + PrefPanesExtensions
                           + InterfaceBuilderExtensions
                           + ScreenSaverExtensions
                           + WebKitExtensions
			   ),
	     packages = packages,
	     package_dir = package_dir,
	     scripts = [ 'Scripts/nibclassbuilder', ],
	     extra_path = "PyObjC",
             **SetupExtraArguments
)

if "install" in sys.argv:
    # Hack to remove a previous version that may have been installed
    # directly into site-packages (pre 0.9) as opposed to a new subdir.
    import shutil
    inst = dist.get_command_obj("install")
    install_dir = inst.install_platlib
    if install_dir is not None:
        for name in ("objc", "Foundation", "AppKit", "AddressBook", "autoGIL"):
            path = os.path.join(install_dir, name)
            if os.path.isdir(path):
                print "(removing old version: %s)" % path
                shutil.rmtree(path)
            elif os.path.isfile(path):
                print "(removing old version: %s)" % path
                os.remove(path)
