#!/usr/bin/env python


import sys
import os
import glob
import site

# Add our utility library to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'setup-lib')))
site.addsitedir(os.path.abspath('source-deps'))

extra_cmdclass = {}
try:
    import pyobjc_mpkg
    extra_cmdclass.update(pyobjc_mpkg.cmdclass)
except ImportError:
    pass

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
from distutils.command.build_ext import build_ext
import os

from di_test import cmd_test
from di_sdist import cmd_sdist


class pyobjc_build_ext (build_ext):
    # Custom build_ext implementation. This differs in two ways from the
    # standard one:
    # 1. We first run the CodeGenerator script
    # 2. We calculate a class-list after building the extensions, and if that
    #    is different from what we had before (e.g. clean install or serious
    #    OS upgrade) we rebuild the extensions.

    def create_empty_class_list(self):
        for fw in ('Fnd', 'App'):
            fd = open('build/codegen/_%s_Classes.inc'%(fw,), 'w')
            fd.write('static const char* gClassNames[] = {\n')
            fd.write('\tNULL\n')
            fd.write('};\n')
            fd.close()

    def create_cached_class_list(self):
        sys.path.insert(0, self.build_lib)
        import objc
        retval = 0

        for pfx, name in (('Fnd', 'Foundation'), ('App', 'AppKit')):
            try:
                m = __import__(name)
            except ImportError:
                continue
            fd = open('build/codegen/_%s_Classes.inc~'%(pfx,), 'w')
            fd.write('static const char* gClassNames[] = {\n')
            for o in m.__dict__.values():
                if not isinstance(o, objc.objc_class): continue
                fd.write('\t"%s",\n'%(o.__name__))
            fd.write('\tNULL\n')
            fd.write('};\n')
            fd.close()

            d1 = open('build/codegen/_%s_Classes.inc~'%(pfx,), 'r').read()
            d2 = open('build/codegen/_%s_Classes.inc'%(pfx,), 'r').read()

            if d1 != d2:
                os.rename(
                        'build/codegen/_%s_Classes.inc~'%(pfx,),
                        'build/codegen/_%s_Classes.inc'%(pfx,)
                    )
                retval = 1


        return retval





    def run(self):
        task_build_libffi()

        # Save self.compiler, we need to reset it when we have to rebuild
        # the extensions.
        compiler_saved = self.compiler

        subprocess("Generating wrappers & stubs", "%s Scripts/CodeGenerators/cocoa_generator.py" % (sys.executable,), None)
        if not os.path.exists('build/codegen/_Fnd_Classes.inc'):
            # Create a dummy classname list, to enable bootstrapping. Don't
            # do this if there already is a list, everything is better than
            # an empty list.
            self.create_empty_class_list()

        build_ext.run(self)

        if self.create_cached_class_list():
            import shutil
            # Note: dependencies don't work here, we depend on a file that
            # probably didn't exist when the glob was done...
            print "** Created a fresh class-cache, rebuilding the extensions"
            if os.path.exists(
                        os.path.join(self.build_temp, 'Modules', 'AppKit')):
                shutil.rmtree(
                        os.path.join(self.build_temp, 'Modules', 'AppKit'))
                os.mkdir(
                        os.path.join(self.build_temp, 'Modules', 'AppKit'))

            if os.path.exists(
                        os.path.join(self.build_temp, 'Modules', 'Foundation')):
                shutil.rmtree(
                        os.path.join(self.build_temp, 'Modules', 'Foundation'))
                os.mkdir(
                        os.path.join(self.build_temp, 'Modules', 'Foundation'))

            try:
                os.unlink(os.path.join(self.build_lib, 'AppKit', '_AppKit.so'))
            except os.error:
                pass

            try:
                os.unlink(os.path.join(self.build_lib, 'Foundation', '_Foundation.so'))
            except os.error:
                pass

            self.compiler = compiler_saved

            build_ext.run(self)

LIBFFI_SOURCES='libffi-src'
if sys.platform != 'darwin' and os.path.exists('/usr/include/ffi.h'):
    # A system with a pre-existing libffi.
    LIBFFI_SOURCES=None

def subprocess(taskName, cmd, validRes=None):
    print "Performing task: %s" % (taskName,)
    fd = os.popen(cmd, 'r')
    for ln in fd.xreadlines():
        sys.stdout.write(ln)

    res = fd.close()
    if res is not validRes:
        sys.stderr.write("Task '%s' failed [%d]\n"%(taskName, res))
        sys.exit(1)

# We need at least Python 2.3
req_ver = (2, 3)

if sys.version_info < req_ver:
    sys.stderr.write('PyObjC: Need at least Python %s\n'%('.'.join(req_ver)))
    sys.exit(1)

if LIBFFI_SOURCES is not None:

    def task_build_libffi():
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

            if ' ' in src_path+inst_dir:
                print >>sys.stderr, "LIBFFI can not build correctly in a path that contains spaces."
                print >>sys.stderr, "This limitation includes the entire path (all parents, etc.)"
                print >>sys.stderr, "Move the PyObjC and libffi source to a path without spaces and build again."
                sys.exit(1)

            inst_dir = inst_dir.replace("'", "'\"'\"'")
            src_path = src_path.replace("'", "'\"'\"'")

            subprocess('Building FFI', "cd build/libffi/BLD && '%s/configure' --prefix='%s' --disable-shared --enable-static && make install"%(src_path, inst_dir), None)

    LIBFFI_BASE='build/libffi'
    LIBFFI_CFLAGS=[
        "-isystem", "%s/include"%LIBFFI_BASE,
    ]
    if os.path.exists('%s/lib/gcc/include/libffi'%LIBFFI_BASE):
        LIBFFI_CFLAGS.extend([
            "-isystem", "%s/lib/gcc/include/libffi"%LIBFFI_BASE,
        ])
    LIBFFI_LDFLAGS=[
        '-L%s/lib'%LIBFFI_BASE, '-lffi',
    ]

else:
    def task_build_libffi():
        pass
    LIBFFI_CFLAGS=[]
    LIBFFI_LDFLAGS=['-lffi']


sourceFiles = [
        "Modules/objc/objc-runtime-apple.m",
        "Modules/objc/objc-runtime-gnu.m",
        "Modules/objc/objc_util.m",
        "Modules/objc/objc_support.m",
        "Modules/objc/class-builder.m",
        "Modules/objc/class-list.m",
        "Modules/objc/ObjCPointer.m",
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
        "Modules/objc/method-signature.m",
        "Modules/objc/module.m",
        "Modules/objc/libffi_support.m",
        "Modules/objc/pointer-support.m",
        "Modules/objc/struct-wrapper.m",
        "Modules/objc/method-imp.m",
        "Modules/objc/bundle-variables.m",
        "Modules/objc/function.m",
]

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
        sys.exit(1)

    CFLAGS=[
        "-DMACOSX",
        "-DAPPLE_RUNTIME",
        "-no-cpp-precomp",
        "-Wno-long-double",
        "-g",

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

    OBJC_LDFLAGS=[
        '-framework', 'Foundation',
        ]

    CF_LDFLAGS=[
        '-framework', 'CoreFoundation', '-framework', 'Foundation',
        ]

    FND_LDFLAGS=[
        '-framework', 'CoreFoundation', '-framework', 'Foundation',
        ]

    APPKIT_LDFLAGS=[
        '-framework', 'CoreFoundation', '-framework', 'AppKit',
        ]

    ADDRESSBOOK_LDFLAGS=[
        '-framework', 'CoreFoundation', '-framework', 'AddressBook', '-framework', 'Foundation',
        ]

    SECURITY_INTERFACE_LDFLAGS=[
        '-framework', 'CoreFoundation', '-framework', 'SecurityInterface', '-framework', 'Foundation',
        ]

    EXCEPTION_HANDLING_LDFLAGS=[
        '-framework', 'CoreFoundation', '-framework', 'ExceptionHandling', '-framework', 'Foundation',
        ]

    PREFPANES_LDFLAGS=[
        '-framework', 'CoreFoundation', '-framework', 'PreferencePanes', '-framework', 'Foundation',
        ]

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

    FND_LDFLAGS=OBJC_LDFLAGS
    FNDMAP_LDFLAGS=OBJC_LDFLAGS
    APPKIT_LDFLAGS=OBJC_LDFLAGS + ['-lgnustep-gui']
    APPMAP_LDFLAGS=OBJC_LDFLAGS + ['-lgnustep-gui']
    CF_LDFLAGS=[]
    ADDRESSBOOK_LDFLAGS=OBJC_LDFLAGS + ['-lAddresses']
    PREFPANES_LDFLAGS=[]
    SECURITY_INTERFACE_LDFLAGS=[]
    EXCEPTION_HANDLING_LDFLAGS=[]

CFLAGS.append('-Ibuild/codegen/')




CorePackages = [ 'objc' ]
CoreExtensions =  [
    Extension("objc._objc",
              sourceFiles,
              extra_compile_args=[
              ] + LIBFFI_CFLAGS + CFLAGS,
              extra_link_args=LIBFFI_LDFLAGS + OBJC_LDFLAGS),
    Extension("objc.test.ctests",
              [ 'Modules/objc/unittest.m' ],
              extra_compile_args=[
              ] + LIBFFI_CFLAGS + CFLAGS,
              extra_link_args=LIBFFI_LDFLAGS + OBJC_LDFLAGS),
    Extension("objc.test.testbndl",
              ["Modules/objc/test/testbndl.m"],
              extra_compile_args=["-IModules/objc" ] + CFLAGS,
              extra_link_args=OBJC_LDFLAGS),
    Extension("objc.test.testbndl2",
              ["Modules/objc/test/testbndl2.m"],
              extra_compile_args=["-IModules/objc" ] + CFLAGS,
              extra_link_args=OBJC_LDFLAGS),
    Extension("objc.test.testclassandinst",
              ["Modules/objc/test/testclassandinst.m"],
              extra_compile_args=["-IModules/objc" ] + CFLAGS,
              extra_link_args=OBJC_LDFLAGS),
    Extension("objc.test.testoutputinitializer",
              ["Modules/objc/test/testoutputinitializer.m"],
              extra_compile_args=["-IModules/objc" ] + CFLAGS,
              extra_link_args=OBJC_LDFLAGS),
    ]

FoundationDepends = {
    'depends': (glob.glob('build/codegen/_Fnd_*.inc')
            + glob.glob('Modules/Foundation/*.m'))
}
AppKitDepends = {
    'depends': (glob.glob('build/codegen/_App_*.inc')
            + glob.glob('Modules/AppKit/*.m'))
}
AddressBookDepends = {
    'depends': glob.glob('build/codegen/*.inc'),
}
CoreFoundationDepends = {
}
SecurityInterfaceDepends = {
    'depends': glob.glob('build/codegen/*.inc'),
}
ExceptionHandlingDepends = {
    'depends': glob.glob('build/codegen/*.inc'),
}
PrefPanesDepends = {
    'depends': glob.glob('build/codegen/*.inc'),
}
InterfaceBuilderDepends = {
    'depends': glob.glob('build/codegen/*.inc'),
}
WebKitDepends = {
    'depends': glob.glob('build/codegen/*.inc'),
}

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
        ], headername="WebKit.h")


def package_version():
    fp = open('Modules/objc/pyobjc.h', 'r')
    for ln in fp.readlines():
        if ln.startswith('#define OBJC_VERSION'):
            fp.close()
            return ln.split()[-1][1:-1]

    raise ValueError, "Version not found"


# skipping CoreFoundationPackages, it's fake!
packages = CorePackages + AppKitPackages + FoundationPackages + AddressBookPackages + PrefPanesPackages + InterfaceBuilderPackages + ScreenSaverPackages + WebKitPackages + MessagePackages + SecurityInterfacePackages + ExceptionHandlingPackages + [ 'PyObjCTools' ]

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
             cmdclass = dict(
                build_ext=pyobjc_build_ext,
                test=cmd_test,
                sdist=cmd_sdist,
                **extra_cmdclass
             ),
             classifiers = [
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
             license = 'MIT License',
             download_url = 'http://pyobjc.sourceforge.net/software/index.php',
)

if "install" in sys.argv:
    # Hack to remove a previous version that may have been installed
    import shutil
    inst = dist.get_command_obj("install")
    install_dir = inst.install_platlib
    if install_dir is not None:
        # clean up cruft from pre 0.9
        for name in ("objc", "Foundation", "AppKit", "AddressBook", "autoGIL"):
            path = os.path.join(install_dir, name)
            if os.path.isdir(path):
                print "(removing old version: %s)" % path
                shutil.rmtree(path)
            elif os.path.isfile(path):
                print "(removing old version: %s)" % path
                os.remove(path)

        # In version 1.2 some of the extension modules moved, clean up the old
        # location
        install_dir = os.path.join(install_dir, 'PyObjC')
        for fn in os.listdir(install_dir):
            fn = os.path.join(install_dir, fn)
            if fn.endswith('.so'):
                os.unlink(fn)
