#!/usr/bin/env python

USE_FFI = 1

USE_FFI_SHORTCUTS = 0

import sys

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

# We need at least Python 2.2
req_ver = [ 2, 2]

if sys.version_info[0] < req_ver[0] or (
        sys.version_info[0] == req_ver[0] 
        and sys.version_info[1] < req_ver[1]):

    sys.stderr.write('PyObjC: Need at least Python %s\n'%('.'.join(req_ver)))
    sys.exit(1)

if USE_FFI:
    if os.environ.has_key('LIBFFI_BASE'):
        LIBFFI_BASE=os.environ['LIBFFI_BASE']
    else:
        LIBFFI_BASE='libffi'
    LIBFFI_CFLAGS=[ 
        "-DOC_WITH_LIBFFI", 
        "-I%s/include"%LIBFFI_BASE, 
    ]
    LIBFFI_LDFLAGS=[ 
        '-read_only_relocs','warning',
        '-L%s/lib'%LIBFFI_BASE, '-lffi', 
    ]
    LIBFFI_SOURCEFILES=[
        'Modules/objc/libffi_support.m',
    ]

    if USE_FFI_SHORTCUTS:
        LIBFFI_CFLAGS.append("-DOC_USE_FFI_SHORTCUTS")
else:
    LIBFFI_CFLAGS=[]
    LIBFFI_LDFLAGS=[]
    LIBFFI_SOURCEFILES=[]

sourceFiles = [
        "Modules/objc/objc_util.m",
        "Modules/objc/objc_support.m",
        "Modules/objc/class-builder.m",
        "Modules/objc/class-list.m",
        "Modules/objc/ObjCPointer.m",
        "Modules/objc/objc-class.m",
        "Modules/objc/informal-protocol.m",
        "Modules/objc/objc-object.m",
        "Modules/objc/super-call.m",
        "Modules/objc/selector.m",
        "Modules/objc/method-accessor.m",
        "Modules/objc/instance-var.m",
        "Modules/objc/OC_PythonInt.m",
        "Modules/objc/OC_PythonObject.m",
        "Modules/objc/OC_PythonString.m",
        "Modules/objc/OC_PythonArray.m",
        "Modules/objc/OC_PythonDictionary.m",
        "Modules/objc/register.m",
        "Modules/objc/pyobjc-api.m",
        "Modules/objc/alloc_hack.m",
        "Modules/objc/module.m",
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
        #"-O0", "-g",
        ]

    OBJC_LDFLAGS=[
        '-framework', 'Foundation',
        ]

    FND_LDFLAGS=[
        '-framework', 'Foundation',
        ]

    APPKIT_LDFLAGS=[
        '-framework', 'AppKit'
        ]

    FNDMAP_LDFLAGS=[
        '-framework', 'Foundation',
        ]

    APPMAP_LDFLAGS=[
        '-framework', 'AppKit'
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
              sourceFiles + LIBFFI_SOURCEFILES,
              extra_compile_args=[
                    "-DOBJC_PARANOIA_MODE",
              ] + LIBFFI_CFLAGS + CFLAGS,
              extra_link_args=LIBFFI_LDFLAGS + OBJC_LDFLAGS),
    Extension("autoGIL", 
              ["Modules/autoGIL.c"],
              extra_compile_args = CFLAGS,
              extra_link_args = ['-framework', 'CoreFoundation']),
    ]
CocoaPackages = [ 'Foundation', 'AppKit' ]
CocoaExtensions = [
          Extension("Foundation._Foundation", 
                    [
                        "Modules/Cocoa/_Foundation.m",
                        "Modules/Cocoa/NSAutoreleasePoolSupport.m"
                    ],
                    extra_compile_args=[
                        "-IModules/objc",  
                    ] + CFLAGS,
                    extra_link_args=[
                    ] + FND_LDFLAGS),
          Extension("AppKit._AppKit", 
                    ["Modules/Cocoa/_AppKit.m"],
                    extra_compile_args=[
                        "-IModules/objc", 
                    ] + CFLAGS,
                    extra_link_args=[
                    ] + APPKIT_LDFLAGS),
          Extension("AppKit._AppKitMapping",
                    ["Modules/Cocoa/_AppKitMapping.m"],
                    extra_compile_args=[ "-IModules/objc",] + CFLAGS,
                    extra_link_args=[] + APPMAP_LDFLAGS),
          Extension("objc._FoundationMapping", 
                    ["Modules/Cocoa/_FoundationMapping.m"],
                    extra_compile_args=[
                        "-IModules/objc", 
                    ] + CFLAGS,
                    extra_link_args=[
                    ] + FNDMAP_LDFLAGS),
      ]

# The AdressBook module is only installed when the user actually has the
# AddressBook framework.
AddressBookPackages, AddressBookExtensions = \
        IfFrameWork('AddressBook.framework', [ 'AddressBook' ], [])


def package_version():
    fp = open('Modules/objc/pyobjc.h', 'r')
    for ln in fp.readlines():
        if ln.startswith('#define OBJC_VERSION'):
            fp.close()
            return ln.split()[-1][1:-1]

    raise ValueError, "Version not found"


packages = CorePackages + CocoaPackages + AddressBookPackages
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
except ImportError:
    # bundlebuilder.py and plistlib.py shipped with newer versions of
    # Python but are included with pyobjc be independent. The following
    # magic makes distutils install the contents of MPCompat.
    packages.append('')
    package_dir[''] = 'MPCompat'

dist = setup(name = "pyobjc",
	     version = package_version(),
	     description = "Python<->ObjC Interoperability Module",
	     author = "bbum, RonaldO, SteveM, LeleG, many others stretching back through the reaches of time...",
	     author_email = "pyobjc-dev@lists.sourceforge.net",
	     url = "http://pyobjc.sourceforge.net/",
	     ext_modules = (
			     CoreExtensions 
			   + CocoaExtensions 
			   + AddressBookExtensions 
			   ),
	     packages = packages,
	     package_dir = package_dir,
	     scripts = [ 'Scripts/nibclassbuilder', ],
	     extra_path = "PyObjC",
)

if "install" in sys.argv:
    # Hack to remove a previous version that may have been installed
    # directly into site-packages (pre 0.9) as opposed to a new subdir.
    import shutil
    inst = dist.get_command_obj("install")
    install_dir = inst.install_platlib
    for name in ("objc", "Foundation", "AppKit", "AddressBook", "autoGIL"):
        path = os.path.join(install_dir, name)
        if os.path.isdir(path):
            print "(removing old version: %s)" % path
            shutil.rmtree(path)
        elif os.path.isfile(path):
            print "(removing old version: %s)" % path
            os.remove(path)
