'''
Wrappers for the "Photos" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension
import os

VERSION="5.1"

setup(
    name='pyobjc-framework-Photos',
    description = "Wrappers for the framework Photos on macOS",
    min_os_level="10.11",
    packages = [ "Photos" ],
    ext_modules = [
        Extension("Photos._Photos",
            [ "Modules/_Photos.m" ],
            extra_link_args=["-framework", "Photos"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_Photos')
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
