'''
Wrappers for the "CoreBluetooth" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

import os
from pyobjc_setup import setup, Extension

setup(
    name='pyobjc-framework-CoreBluetooth',
    version="3.1b1",
    description = "Wrappers for the framework CoreBluetooth on Mac OS X",
    long_description=__doc__,
    packages = [ "CoreBluetooth" ],
    setup_requires = [
        'pyobjc-core>=3.1b1',
    ],
    install_requires = [
        'pyobjc-core>=3.1b1',
        'pyobjc-framework-Cocoa>=3.1b1',
    ],
    min_os_level="10.10",
    ext_modules = [
        Extension("CoreBluetooth._CoreBluetooth",
            [ "Modules/_CoreBluetooth.m" ],
            extra_link_args=["-framework", "CoreBluetooth"],
            depends=[
                os.path.join('Modules', fn)
                    for fn in os.listdir('Modules')
                    if fn.startswith('_CoreBluetooth')
            ]
        ),
    ],
)
