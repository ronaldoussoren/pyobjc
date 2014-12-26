'''
Wrappers for the "StoreKit" framework on MacOS X 10.7 or later.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

setup(
    name='pyobjc-framework-StoreKit',
    version="3.1b1",
    description = "Wrappers for the framework StoreKit on Mac OS X",
    long_description=__doc__,
    packages = [ "StoreKit" ],
    setup_requires = [
        'pyobjc-core>=3.1b1',
    ],
    install_requires = [
        'pyobjc-core>=3.1b1',
        'pyobjc-framework-Cocoa>=3.1b1',
    ],
    ext_modules = [
        Extension("StoreKit._StoreKit",
            [ "Modules/_StoreKit.m" ],
            extra_link_args=["-framework", "StoreKit"],
            depends=[
                os.path.join('Modules', fn)
                    for fn in os.listdir('Modules')
                    if fn.startswith('_StoreKit')
            ]
        ),
    ],
    min_os_level='10.7',
)
