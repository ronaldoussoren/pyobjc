"""
Utilities that are helpfull for building pyobjc based framework
wrappers.
"""
__all__ = ('build_cmd_for_min_os_level', 'pyobjc_extra_compile_args')
from distutils.command.build import build as _build_cmd
from distutils.errors import DistutilsPlatformError
import platform

class build_unsupported (_build_cmd):
    def run(self):
        raise DistutilsPlatformError(
            "Building this distribution is not supported on this version os MacOSX")


def build_cmd_for_min_os_level(os_level):
    import platform

    cur_level = '.'.join(platform.mac_ver()[0].split('.')[:2])
    if cur_level < os_level:
        return build_unsupported
    else:
        return _build_cmd


def pyobjc_extra_compile_args():
    cur_level = '.'.join(platform.mac_ver()[0].split('.')[:2])
    result =  ["-DPyObjC_BUILD_RELEASE=%02d%02d"%(tuple(map(int, platform.mac_ver()[0].split('.')[:2])))]
    if cur_level == '10.4':
        result.extend(['-isysroot','/'])
    return result
