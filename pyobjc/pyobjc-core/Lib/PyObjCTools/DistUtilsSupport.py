"""
Utilities that are helpfull for building pyobjc based framework
wrappers.
"""
__all__ = ('build_cmd_for_min_os_level', 'pyobjc_extra_compile_args')
from distutils.core import Command
from distutils.errors import DistutilsPlatformError
import platform

class build_unsupported (Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass

    def run(self):
        raise DistutilsPlatformError(
            "Building this distribution is not supported on this version os MacOSX")


def insert_extra_cmd(extra_cmd, os_level=None):
    import platform

    if os_level is None:
        return

    cur_level = '.'.join(platform.mac_ver()[0].split('.')[:2])
    if cur_level < os_level:
        extra_cmd['test']    = build_unsupported
        extra_cmd['build']   = build_unsupported
        extra_cmd['install'] = build_unsupported
        extra_cmd['develop'] = build_unsupported

def pyobjc_extra_compile_args():
    cur_level = '.'.join(platform.mac_ver()[0].split('.')[:2])
    result =  ["-DPyObjC_BUILD_RELEASE=%02d%02d"%(tuple(map(int, platform.mac_ver()[0].split('.')[:2])))]
    if cur_level == '10.4':
        result.extend(['-isysroot','/'])
    return result
