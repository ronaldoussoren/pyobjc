'''
Wrappers for the "ModelIO" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="3.2a1"

setup(
    name='pyobjc-framework-ModelIO',
    version="3.2",
    description = "Wrappers for the framework ModelIO on Mac OS X",
    long_description=__doc__,
    packages = [ "ModelIO" ],
    setup_requires = [
        'pyobjc-core>=3.2',
    ],
    install_requires = [
        'pyobjc-core>=3.2',
        'pyobjc-framework-Cocoa>=3.2',
        'pyobjc-framework-Quartz>=3.2',
    ],
    min_os_level="10.11",
    ext_modules = [
        Extension("ModelIO._ModelIO",
            [ "Modules/_ModelIO.m" ],
            extra_link_args=["-framework", "ModelIO"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_ModelIO')
            ]
        ),
    ],
)
