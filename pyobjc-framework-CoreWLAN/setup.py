'''
Wrappers for the "CoreWLAN" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

import os
from pyobjc_setup import setup, Extension

setup(
    name='pyobjc-framework-CoreWLAN',
    version="3.1b1",
    description = "Wrappers for the framework CoreWLAN on Mac OS X",
    long_description=__doc__,
    packages = [ "CoreWLAN" ],
    setup_requires = [
        'pyobjc-core>=3.1b1',
    ],
    install_requires = [
        'pyobjc-core>=3.1b1',
        'pyobjc-framework-Cocoa>=3.1b1',
    ],
    ext_modules = [
        Extension("CoreWLAN._CoreWLAN",
            [ "Modules/_CoreWLAN.m" ],
            extra_link_args=["-framework", "CoreWLAN"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_CoreWLAN')
            ]
        ),
    ],
    min_os_level="10.6",
)
