import os
import sys, platform
import shutil
from distutils.cmd import Command
from distutils.util import get_platform
from distutils.errors import *
from pyobjc_setup_utils import runtasks

class build_libffi(Command):
    description = "build libffi"
    user_options = [
        ('libffi-sources=', None,
        "location of libffi sources (defaults to \"libffi-src\")"),
    ]

    def initialize_options(self):
        self.finalized = False
        if sys.platform != 'darwin' and os.path.exists('/usr/include/ffi.h'):
            self.libffi_sources = None
        else:
            self.libffi_sources = 'libffi-src'

    def finalize_options(self):
        if self.libffi_sources is not None:
            self.libffi_sources = os.path.abspath(self.libffi_sources)
            if not os.path.isdir(self.libffi_sources):
                print >>sys.stderr, "LIBFFI_SOURCES is not a directory: %s" % (self.libffi_sources,)
                print >>sys.stderr, "\tSee Install.txt or Install.html for more information."
                raise DistutilsFileError('LIBFFI_SOURCES is not a directory')
            build_base = os.path.abspath(self.reinitialize_command('build').build_base)
            base = self.libffi_base = os.path.join(build_base, 'libffi.' + get_platform())
            self.cflags = ["-isystem", os.path.join(base, "include")]
            extra = os.path.join(base, 'lib', 'gcc', 'include', 'libffi')
            if os.path.exists(extra):
                self.cflags.extend(['-isystem', extra])
            self.ldflags = ['-L' + os.path.join(base, 'lib'), '-lffi']
        else:
            self.cflags = []
            self.ldflags = ['-lffi']
        self.finalized = True

    def run(self):
        self.finalize_options()
        if self.libffi_sources is not None:
            inst_dir = self.libffi_base
            build_dir = os.path.join(inst_dir, 'BLD')
            if not os.path.exists(build_dir):
                os.makedirs(build_dir)

            if not os.path.exists(os.path.join(inst_dir, 'lib', 'libffi.a')):
                # No pre-build version available, build it now.
                # Do not use a relative path for the build-tree, libtool on
                # MacOS X doesn't like that.

                cflags = os.environ.get('CFLAGS', None)
                if sys.platform == 'darwin' and platform.machine() != 'Power Macintosh':
                    os.environ['CFLAGS'] = '-O3 -fPIC'

                runtasks('Building FFI',
                    [os.path.join(self.libffi_sources, 'configure'),
                        '--prefix=' + inst_dir, '--disable-shared', '--enable-static'],
                    ['make', 'install'],
                    cwd=build_dir)

                if cflags is not None:
                    os.environ['CFLAGS'] = cflags
                elif 'CFLAGS' in os.environ:
                    del os.environ['CFLAGS']

                # make sure cflags is set correctly
                self.finalize_options()

cmdclass = dict(build_libffi=build_libffi)
