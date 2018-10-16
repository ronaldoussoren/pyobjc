'''
Wrappers for the "CoreSpotlight" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="5.1"

setup(
    name='pyobjc-framework-CoreSpotlight',
    description = "Wrappers for the framework CoreSpotlight on macOS",
    min_os_level="10.13",
    packages = [ "CoreSpotlight" ],
    ext_modules = [
        Extension("CoreSpotlight._CoreSpotlight",
            [ "Modules/_CoreSpotlight.m" ],
            extra_link_args=["-framework", "CoreSpotlight"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_CoreSpotlight')
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
