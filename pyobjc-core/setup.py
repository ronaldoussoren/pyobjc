#!/usr/bin/env python

import sys
import subprocess
import shutil
import re
import os
import plistlib

# We need at least Python 2.5
MIN_PYTHON = (2, 6)

# FIXME: autodetect default values for USE_* variables:
#  both should be false by default, unless
#  1) python is /usr/bin/python: both should be true
#  2) python build with --with-system-libffi: USE_SYSTEM_FFI
#     should be true.

# Set USE_SYSTEM_FFI to True to link to the system version
# of libffi
USE_SYSTEM_FFI = False

if sys.version_info < MIN_PYTHON:
    vstr = '.'.join(map(str, MIN_PYTHON))
    raise SystemExit('PyObjC: Need at least Python ' + vstr)


try:
    import setuptools

except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()


#extra_args=dict(
    #use_2to3 = True,
#)

def get_os_level():
    pl = plistlib.readPlist('/System/Library/CoreServices/SystemVersion.plist')
    v = pl['ProductVersion']
    return '.'.join(v.split('.')[:2])





from setuptools.command import build_py
from setuptools.command import test
from distutils import log
from distutils.core import Command


class oc_build_py (build_py.build_py):
    def run_2to3(self, files, doctests=True):
        files = [ fn for fn in files if not os.path.basename(fn).startswith('test3_') ]
        build_py.build_py.run_2to3(self, files, doctests)

    def build_packages(self):
        log.info("Overriding build_packages to copy PyObjCTest")        
        p = self.packages
        self.packages = list(self.packages) + ['PyObjCTest']
        try:
            build_py.build_py.build_packages(self)
        finally:
            self.packages = p

from pkg_resources import working_set, normalize_path, add_activation_listener, require

class oc_test (test.test):
    description = "run test suite"
    user_options = [
        ('verbosity=', None, "print what tests are run"),
    ]

    def initialize_options(self):
        self.verbosity='1'

    def finalize_options(self):
        if isinstance(self.verbosity, str):
            self.verbosity = int(self.verbosity)


    def cleanup_environment(self):
        ei_cmd = self.get_finalized_command('egg_info')
        egg_name = ei_cmd.egg_name.replace('-', '_')

        to_remove =  []
        for dirname in sys.path:
            bn = os.path.basename(dirname)
            if bn.startswith(egg_name + "-"):
                to_remove.append(dirname)

        for dirname in to_remove:
            log.info("removing installed %r from sys.path before testing"%(
                dirname,))
            sys.path.remove(dirname)

        from pkg_resources import add_activation_listener
        add_activation_listener(lambda dist: dist.activate())
        working_set.__init__()

    def add_project_to_sys_path(self):
        from pkg_resources import normalize_path, add_activation_listener
        from pkg_resources import working_set, require

        if getattr(self.distribution, 'use_2to3', False):

            # Using 2to3, cannot do this inplace:
            self.reinitialize_command('build_py', inplace=0)
            self.run_command('build_py')
            bpy_cmd = self.get_finalized_command("build_py")
            build_path = normalize_path(bpy_cmd.build_lib)

            self.reinitialize_command('egg_info', egg_base=build_path)
            self.run_command('egg_info')

            self.reinitialize_command('build_ext', inplace=0)
            self.run_command('build_ext')

        else:
            self.reinitialize_command('egg_info')
            self.run_command('egg_info')
            self.reinitialize_command('build_ext', inplace=1)
            self.run_command('build_ext')
        
        self.__old_path = sys.path[:]
        self.__old_modules = sys.modules.copy()

        if 'PyObjCTools' in sys.modules:
            del sys.modules['PyObjCTools']


        ei_cmd = self.get_finalized_command('egg_info')
        sys.path.insert(0, normalize_path(ei_cmd.egg_base))
        sys.path.insert(1, os.path.dirname(__file__))
            
        add_activation_listener(lambda dist: dist.activate())
        working_set.__init__()
        require('%s==%s'%(ei_cmd.egg_name, ei_cmd.egg_version))

    def remove_from_sys_path(self):
        from pkg_resources import working_set
        sys.path[:] = self.__old_path
        sys.modules.clear()
        sys.modules.update(self.__old_modules)
        working_set.__init__()


    def run(self):
        import unittest

        # Ensure that build directory is on sys.path (py3k)
        import sys

        self.cleanup_environment()
        self.add_project_to_sys_path()

        from PyObjCTest.loader import makeTestSuite
        import PyObjCTools.TestSupport as mod

        try:
            meta = self.distribution.metadata
            name = meta.get_name()
            test_pkg = name + "_tests"
            suite = makeTestSuite()

            runner = unittest.TextTestRunner(verbosity=self.verbosity)
            result = runner.run(suite)

            # Print out summary. This is a structured format that
            # should make it easy to use this information in scripts.
            summary = dict(
                count=result.testsRun,
                fails=len(result.failures),
                errors=len(result.errors),
                xfails=len(getattr(result, 'expectedFailures', [])),
                xpass=len(getattr(result, 'expectedSuccesses', [])),
                skip=len(getattr(result, 'skipped', [])),
            )
            print("SUMMARY: %s"%(summary,))

        finally:
            self.remove_from_sys_path()

from setuptools.command import egg_info

def write_header(cmd, basename, filename):
    with open(os.path.join('Modules/objc/', os.path.basename(basename)), 'rU') as fp:
        data = fp.read()
    if not cmd.dry_run:
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

    cmd.write_file(basename, filename, data)


# This is a workaround for a bug in setuptools: I'd like
# to use the 'egg_info.writers' entry points in the setup()
# call, but those don't work when also using a package_base
# argument as we do.
# (issue 123 in the distribute tracker)
class my_egg_info (egg_info.egg_info):
    def run(self):
        egg_info.egg_info.run(self)

        for hdr in ("pyobjc-compat.h", "pyobjc-api.h"):
            fn = os.path.join("include", hdr)

            write_header(self, fn, os.path.join(self.egg_info, fn))

if sys.version_info[0] == 3:
    # FIXME: add custom test command that does the work.
    # - Patch sys.path
    # - Ensure PyObjCTest gets translated by 2to3
    from distutils.util import get_platform
    build_dir = 'build/lib.%s-%d.%d'%(
        get_platform(), sys.version_info[0], sys.version_info[1])
    if hasattr(sys, 'gettotalrefcount'):
        build_dir += '-pydebug'
    sys.path.insert(0,  build_dir)


import os
import glob
import site
import platform

if 'MallocStackLogging' in os.environ:
    del os.environ['MallocStackLogging']
if 'MallocStackLoggingNoCompact' in os.environ:
    del os.environ['MallocStackLoggingNoCompact']

# See the news file:
#os.environ['MACOSX_DEPLOYMENT_TARGET']='10.5'



#if int(os.uname()[2].split('.')[0]) >= 10:
#        USE_SYSTEM_FFI = True


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

PyObjC requires MacOS X 10.4 or later.  This beta release requires
MacOS X 10.5.
"""

from setuptools import setup, Extension, find_packages
from setuptools.command import build_ext, install_lib
import os

class pyobjc_install_lib (install_lib.install_lib):
    def get_exclusions(self):
        result = install_lib.install_lib.get_exclusions(self)
        for fn in install_lib._install_lib.get_outputs(self):
            if 'PyObjCTest' in fn:
                result[fn] = 1

        for fn in os.listdir('PyObjCTest'):
            result[os.path.join('PyObjCTest', fn)] = 1
            result[os.path.join(self.install_dir, 'PyObjCTest', fn)] = 1


        return result

class pyobjc_build_ext (build_ext.build_ext):
    def run(self):
        build_ext.build_ext.run(self)
        extensions = self.extensions
        self.extensions = [
                e for e in extensions if e.name.startswith('PyObjCTest') ]
        self.copy_extensions_to_source()
        self.extensions = extensions

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
    print("You're not running on MacOS X, and don't use GNUstep")
    print("I don't know how to build PyObjC on such a platform.")
    print("Please read the ReadMe.")
    print("")
    raise SystemExit("ObjC runtime not found")

from distutils.sysconfig import get_config_var, get_config_vars

CFLAGS=[ ]

# Enable 'PyObjC_STRICT_DEBUGGING' to enable some costly internal 
# assertions. 
CFLAGS.extend([
    
    # Use this to analyze with clang
    #"--analyze",

# The following flags are an attempt at getting rid of /usr/local
# in the compiler search path.
    "-DPyObjC_STRICT_DEBUGGING",
    "-DMACOSX", # For libffi
    "-DPyObjC_BUILD_RELEASE=%02d%02d"%(tuple(map(int, platform.mac_ver()[0].split('.')[:2]))),
#    "-no-cpp-precomp",
    "-DMACOSX",
    "-g",
    "-fexceptions",


    # Loads of warning flags
    "-Wall", "-Wstrict-prototypes", "-Wmissing-prototypes",
    "-Wformat=2", "-W", 
    #"-Wshadow", # disabled due to warnings from Python headers
    "-Wpointer-arith", #"-Wwrite-strings",
    "-Wmissing-declarations",
    "-Wnested-externs",
#    "-Wno-long-long",
    "-W",

    #"-fcatch-undefined-behavior",
    #"-Wno-missing-method-return-type", # XXX
    "-Wno-import",
    "-DPyObjC_BUILD_RELEASE=%02d%02d"%(tuple(map(int, get_os_level().split('.')))),
    #"-Warray-bounds", # XXX: Needed to avoid False positives for PyTuple access macros
    ])

## Arghh, a stupid compiler flag can cause problems. Don't 
## enable -O0 if you value your sanity. With -O0 PyObjC will crash
## on i386 systems when a method returns a struct that isn't returned
## in registers. 
if '-O0' in get_config_var('CFLAGS'):
    print ("Change -O0 to -O1")
    vars = get_config_vars()
    vars['CFLAGS'] = vars['CFLAGS'].replace('-O0', '-O1')

OBJC_LDFLAGS = frameworks('CoreFoundation', 'Foundation', 'Carbon')

if not os.path.exists('/usr/include/objc/runtime.h'):
    CFLAGS.append('-DNO_OBJC2_RUNTIME')

# Force compilation with the local SDK, compilation of PyObC will result in
# a binary that runs on other releases of the OS without using a particular SDK.
CFLAGS.extend(['-isysroot', '/'])
OBJC_LDFLAGS.extend(['-isysroot', '/'])



CFLAGS.append('-Ibuild/codegen/')

# Patch distutils: it needs to compile .S files as well.
from distutils.unixccompiler import UnixCCompiler
UnixCCompiler.src_extensions.append('.S')
del UnixCCompiler


# 
# Support for an embedded copy of libffi
#
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



#
# Calculate the list of extensions: objc._objc + extensions for the unittests
#

if USE_SYSTEM_FFI:
    ExtensionList =  [ 
        Extension("objc._objc",
            list(glob.glob(os.path.join('Modules', 'objc', '*.m'))),
            extra_compile_args=CFLAGS + ["-I/usr/include/ffi"],
            extra_link_args=OBJC_LDFLAGS + ["-lffi"],
            depends=list(glob.glob(os.path.join('Modules', 'objc', '*.h'))),
        ),
    ]

else:
    ExtensionList =  [ 
        Extension("objc._objc",
            FFI_SOURCE + list(glob.glob(os.path.join('Modules', 'objc', '*.m'))),
            extra_compile_args=CFLAGS + FFI_CFLAGS,
            extra_link_args=OBJC_LDFLAGS,
            depends=list(glob.glob(os.path.join('Modules', 'objc', '*.h'))),
        ),
    ]

for test_source in glob.glob(os.path.join('Modules', 'objc', 'test', '*.m')):
    name, ext = os.path.splitext(os.path.basename(test_source))

    ExtensionList.append(Extension('PyObjCTest.' + name,
        [test_source],
        extra_compile_args=['-IModules/objc'] + CFLAGS,
        extra_link_args=OBJC_LDFLAGS))

def package_version():
    fp = open('Modules/objc/pyobjc.h', 'r')
    for ln in fp.readlines():
        if ln.startswith('#define OBJC_VERSION'):
            fp.close()
            return ln.split()[-1][1:-1]

    raise ValueError("Version not found")

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


dist = setup(
    name = "pyobjc-core", 
    version = package_version(),
    description = "Python<->ObjC Interoperability Module",
    long_description = LONG_DESCRIPTION,
    author = "Ronald Oussoren, bbum, SteveM, LeleG, many others stretching back through the reaches of time...",
    author_email = "pyobjc-dev@lists.sourceforge.net",
    url = "http://pyobjc.sourceforge.net/",
    platforms = [ 'MacOS X' ],
    ext_modules = ExtensionList,
    packages = [ 'objc', 'PyObjCTools', ], 
    namespace_packages = ['PyObjCTools'],
    package_dir = { '': 'Lib', 'PyObjCTest': 'PyObjCTest' },
    extra_path = "PyObjC",
    cmdclass = {'build_ext': pyobjc_build_ext, 'install_lib': pyobjc_install_lib, 'build_py': oc_build_py, 'test': oc_test, 'egg_info':my_egg_info },
    options = {'egg_info': {'egg_base': 'Lib'}},
    classifiers = CLASSIFIERS,
    license = 'MIT License',
    download_url = 'http://pyobjc.sourceforge.net/software/index.php',
    zip_safe = False,
)
