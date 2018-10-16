'''
Wrappers for the "MultipeerConnectivity" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="5.1"

setup(
    name='pyobjc-framework-MultipeerConnectivity',
    description = "Wrappers for the framework MultipeerConnectivity on macOS",
    min_os_level="10.10",
    packages = [ "MultipeerConnectivity" ],
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
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
