'''
Wrappers for the "MultipeerConnectivity" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

setup(
    name='pyobjc-framework-MultipeerConnectivity',
    version="3.1b1",
    description = "Wrappers for the framework MultipeerConnectivity on Mac OS X",
    long_description=__doc__,
    packages = [ "MultipeerConnectivity" ],
    setup_requires = [
        'pyobjc-core>=3.1b1',
    ],
    install_requires = [
        'pyobjc-core>=3.1b1',
        'pyobjc-framework-Cocoa>=3.1b1',
    ],
    ext_modules = [
        Extension("MultipeerConnectivity._MultipeerConnectivity",
            [ "Modules/_MultipeerConnectivity.m" ],
            extra_link_args=["-framework", "MultipeerConnectivity"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_MultipeerConnectivity')
            ]
        ),
    ],
    min_os_level="10.10",
)
