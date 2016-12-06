'''
Wrappers for the "ImageCaptureCore" framework on Mac OS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
import os
from pyobjc_setup import setup, Extension

VERSION="3.2a1"

setup(
    name='pyobjc-framework-ImageCaptureCore',
    version="3.3a0",
    description = "Wrappers for the framework ImageCaptureCore on Mac OS X",
    long_description=__doc__,
    packages = [ "ImageCaptureCore" ],
    setup_requires = [
        'pyobjc-core>=3.3a0',
    ],
    install_requires = [
        'pyobjc-core>=3.3a0',
        'pyobjc-framework-Cocoa>=3.3a0',
    ],
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
)
