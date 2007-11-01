#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()

import sys
import os
import glob
import site

# See the news file:
#os.environ['MACOSX_DEPLOYMENT_TARGET']='10.5'

# We need at least Python 2.3
MIN_PYTHON = (2, 3)

if sys.version_info < MIN_PYTHON:
    vstr = '.'.join(map(str, MIN_PYTHON))
    raise SystemExit('PyObjC: Need at least Python ' + vstr)

# Add our dependencies to the path.
site.addsitedir(os.path.abspath('source-deps'))

# Add our utility library to the path
sys.path.insert(1, os.path.abspath('setup-lib'))

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

from setuptools import setup, Extension, find_packages
import os


def frameworks(*args):
    lst = []
    for arg in args:
        lst.extend(['-framework', arg])
    return lst

def IfFrameWork(name, packages, extensions, headername=None):
    """
    Return the packages and extensions if the framework exists, or
    two empty lists if not.
    """
    import os
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
    "-DPyObjC_STRICT_DEBUGGING",
    "-DMACOSX",
    "-no-cpp-precomp",
    "-Wno-long-double",
    #"-Wselector",
    "-g",
    #"-fobjc-gc",

    ## Arghh, a stupid compiler flag can cause problems. Don't 
    ## enable -O0 if you value your sanity. With -O0 PyObjC will crash
    ## on i386 systems when a method returns a struct that isn't returned
    ## in registers. 
    #"-O0",
    "-O1",
    #"-O2",
    #"-O3",

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



if not os.path.exists('/usr/include/objc/runtime.h'):
    CFLAGS.append('-DNO_OBJC2_RUNTIME')


OBJC_LDFLAGS = frameworks('CoreFoundation', 'Foundation', 'Carbon')
FND_LDFLAGS = frameworks('CoreFoundation', 'Foundation')
APPKIT_LDFLAGS = frameworks('CoreFoundation', 'AppKit')

# We're using xml2, check for the flags to use:
def xml2config(arg):
    import os, shlex
    ln = os.popen('xml2-config %s'%(arg,), 'r').readline()
    ln = ln.strip()

    return shlex.split(ln)

CFLAGS.extend(xml2config('--cflags'))
OBJC_LDFLAGS.extend(xml2config('--libs'))


BASE_LDFLAGS = []

CFLAGS.append('-Ibuild/codegen/')

# Patch distutils: it needs to compile .S files as well.
from distutils.unixccompiler import UnixCCompiler
UnixCCompiler.src_extensions.append('.S')
del UnixCCompiler

# XXX: the second -I shouldn't be necessary, but somehow is.
FFI_CFLAGS=['-Ilibffi-src/include', '-Ilibffi-src/powerpc']

# The list below includes the source files for all CPU types that we run on
# this makes it easier to build fat binaries on Mac OS X.
FFI_SOURCE=[
    "libffi-src/ffi.c",
    "libffi-src/types.c",
    "libffi-src/powerpc/ppc-darwin.S",
    "libffi-src/powerpc/ppc-darwin_closure.S",
    "libffi-src/powerpc/ppc-ffi_darwin.c",
    "libffi-src/powerpc/ppc64-darwin_closure.S",
    "libffi-src/x86/darwin64.S",
    "libffi-src/x86/x86-darwin.S",
    "libffi-src/x86/x86-ffi64.c",
    "libffi-src/x86/x86-ffi_darwin.c",
]

EXTRA_SOURCE = FFI_SOURCE
EXTRA_CFLAGS = FFI_CFLAGS

CorePackages = [ 'objc' ]
objcExtension = Extension("objc._objc",
    EXTRA_SOURCE + list(glob.glob(os.path.join('Modules', 'objc', '*.m'))),
    extra_compile_args=CFLAGS + EXTRA_CFLAGS,
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
            [test_source],
            extra_compile_args=['-IModules/objc'] + CFLAGS,
            extra_link_args=OBJC_LDFLAGS + BASE_LDFLAGS)

    CoreExtensions.append(ext)


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

def package_version():
    fp = open('Modules/objc/pyobjc.h', 'r')
    for ln in fp.readlines():
        if ln.startswith('#define OBJC_VERSION'):
            fp.close()
            return ln.split()[-1][1:-1]

    raise ValueError, "Version not found"


#packages = (
#    CorePackages +
#    AppKitPackages +
#    FoundationPackages +
#
#    [
#        'PyObjCTools',
#        'PyObjCTools.XcodeSupport',
#    ]
#)



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

install_requires = setup_requires = ['py2app>=0.4.0', 'bdist_mpkg>=0.4.2']

dist = setup(
    name = "pyobjc-core", 
    version = package_version(),
    description = "Python<->ObjC Interoperability Module",
    long_description = LONG_DESCRIPTION,
    author = "bbum, RonaldO, SteveM, LeleG, many others stretching back through the reaches of time...",
    author_email = "pyobjc-dev@lists.sourceforge.net",
    url = "http://pyobjc.sourceforge.net/",
    platforms = [ 'MacOS X' ],
    ext_modules = (
         CoreExtensions
    ),
    packages = [ 'objc', 'objc.test', 'PyObjCTools' ], # 'ExceptionHandling'
    namespace_packages = ['PyObjCTools'],
    package_dir = { '': 'Lib' },
    install_requires = install_requires,
    setup_requires = setup_requires,
    extra_path = "PyObjC",
    cmdclass = extra_cmdclass,
    options = OPTIONS,
    classifiers = CLASSIFIERS,
    license = 'MIT License',
    download_url = 'http://pyobjc.sourceforge.net/software/index.php',
    zip_safe = False,
    # workaround for setuptools 0.6b4 bug
    dependency_links = [],
    package_data = {
        # Include embedded BridgeSuport.xml fallback metadata.
        '': ['*.bridgesupport'],
    }
)

if 0 and 'install' in sys.argv:
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
