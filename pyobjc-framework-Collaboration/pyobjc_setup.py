"""
Generic setup.py file for PyObjC framework wrappers.

This file should only be changed in pyobjc-core and then copied
to all framework wrappers.
"""

__all__ = ('setup', 'Extension', 'Command')

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup as _setup, Extension as _Extension, Command
from distutils.errors import DistutilsPlatformError
from distutils.command import build, install, install_lib
from setuptools.command import develop, test, build_ext
import plistlib
import sys
import __main__

def get_os_level():
    pl = plistlib.readPlist('/System/Library/CoreServices/SystemVersion.plist')
    v = pl['ProductVersion']
    return '.'.join(v.split('.')[:2])

class pyobjc_install_lib (install_lib.install_lib):
    def get_exclusions(self):
        result = install_lib.install_lib.get_exclusions(self)
        for fn in install_lib._install_lib.get_outputs(self):
            if 'PyObjCTest' in fn:
                result[fn] = 1

        return result

class pyobjc_build_ext (build_ext.build_ext):
    def run(self):
        build_ext.build_ext.run(self)
        extensions = self.extensions
        self.extensions = [
            e for e in extensions if e.name.startswith('PyObjCTest') ]
        self.copy_extensions_to_source()
        self.extensions = extensions



def Extension(*args, **kwds):
    """
    Simple wrapper about distutils.core.Extension that adds additional PyObjC 
    specific flags.
    """
    os_level = get_os_level()
    cflags =  ["-DPyObjC_BUILD_RELEASE=%02d%02d"%(tuple(map(int, os_level.split('.'))))]
    ldflags = []
    if os_level != '10.4':
        cflags.extend(['-isysroot','/'])
        ldflags.extend(['-isysroot','/'])
    else:
        cflags.append('-DNO_OBJC2_RUNTIME')

    if 'extra_compile_args' in kwds:
        kwds['extra_compile_args'] = kwds['extra_compile_args'] + cflags
    else:
        kwds['extra_compile_args'] = cflags

    if 'extra_link_args' in kwds:
        kwds['extra_link_args'] = kwds['extra_link_args'] + ldflags
    else:
        kwds['extra_link_args'] = ldflags

    return _Extension(*args, **kwds)


def setup(
        min_os_level=None,
        max_os_level=None,
        cmdclass=None,
        **kwds):

    os_level = get_os_level()
    os_compatible = True
    if sys.platform != 'darwin':
        os_compatible = False

    else:
        if min_os_level is not None:
            if os_level < min_os_level:
                os_compatible = False
        if max_os_level is not None:
            if os_level > max_os_level:
                os_compatible = False

    if cmdclass is None:
        cmdclass = {}
    else:
        cmdclass = cmdclass.copy()

    if not os_compatible:
        def create_command_subclass(base_class):
            if min_os_level != None:
                if max_os_level != None:
                    msg = "This distribution is only supported on MacOSX versions %s upto and including %s"%(
                            min_os_level, max_os_level)
                else:
                    msg = "This distribution is only support on MacOSX >= %s"%(min_os_level,)
            elif max_os_level != None:
                    msg = "This distribution is only support on MacOSX <= %s"%(max_os_level,)
            else:
                    msg = "This distribution is only support on MacOSX"

            class subcommand (base_class):
                def run(self):
                    raise DistutilsPlatformError(msg)

            return subcommand

        cmdclass['build'] = create_command_subclass(build.build)
        cmdclass['test'] = create_command_subclass(test.test)
        cmdclass['install'] = create_command_subclass(install.install)
        cmdclass['develop'] = create_command_subclass(develop.develop)
    else:
        cmdclass['build_ext'] = pyobjc_build_ext
        cmdclass['install_lib'] = pyobjc_install_lib

    _setup(
        cmdclass=cmdclass, 
        long_description=__main__.__doc__,
        author='Ronald Oussoren',
        author_email='pyobjc-dev@lists.sourceforge.net',
        url='http://pyobjc.sourceforge.net',
        platforms = [ "MacOS X" ],
        package_dir = { '': 'Lib', 'PyObjCTest': 'PyObjCTest' },
        dependency_links = [],
        package_data = { '': ['*.bridgesupport'] },
        test_suite='PyObjCTest',
        zip_safe = True,
        **kwds
    ) 
