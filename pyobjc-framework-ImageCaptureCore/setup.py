'''
Wrappers for the "ImageCaptureCore" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
import os
from pyobjc_setup import setup, Extension

VERSION="5.1"

setup(
    name='pyobjc-framework-ImageCaptureCore',
    description = "Wrappers for the framework ImageCaptureCore on macOS",
    min_os_level='10.6',
    packages = [ "ImageCaptureCore" ],
    ext_modules = [
        Extension("ImageCaptureCore._ImageCaptureCore",
            [ "Modules/_ImageCaptureCore.m" ],
            extra_link_args=["-framework", "ImageCaptureCore"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_ImageCaptureCore')
            ]
        ),
    ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
