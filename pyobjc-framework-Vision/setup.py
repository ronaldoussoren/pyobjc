'''
Wrappers for the "Vision" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="5.1"

setup(
    name='pyobjc-framework-Vision',
    description = "Wrappers for the framework Vision on macOS",
    min_os_level="10.13",
    packages = [ "Vision" ],
    ext_modules = [
        Extension("Vision._Vision",
            [ "Modules/_Vision.m" ],
            extra_link_args=["-framework", "Vision"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_Vision')
            ]
        ),
    ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
        'pyobjc-framework-Quartz>='+VERSION,
        'pyobjc-framework-CoreML>='+VERSION,
    ],
    long_description=__doc__,
)
