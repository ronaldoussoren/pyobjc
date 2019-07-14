'''
Wrappers for the "Logging" framework on macOS 10.15 and later.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="6.0a0"

setup(
    name='pyobjc-framework-Logging',
    description = "Wrappers for the framework Logging on macOS",
    min_os_level="10.15",
    packages = [ "Logging" ],
    ext_modules = [
        Extension("Logging._Logging",
            [ "Modules/_Logging.m" ],
            extra_link_args=["-framework", "Logging"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_Logging')
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
