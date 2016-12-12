'''
Wrappers for the "IOSurface" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup
import os

VERSION="3.3a0"

setup(
    name='pyobjc-framework-IOSurface',
    description = "Wrappers for the framework IOSurface on Mac OS X",
    min_os_level="10.6",
    packages = [ "IOSurface" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
