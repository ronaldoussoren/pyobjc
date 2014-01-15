'''
Wrappers for the "DiskArbitration" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

setup(
    name='pyobjc-framework-DiskArbitration',
    version="3.0a1",
    description = "Wrappers for the framework DiskArbitration on Mac OS X",
    packages = [ "DiskArbitration" ],
    setup_requires = [
        'pyobjc-core>=3.0a1',
    ],
    install_requires = [
        'pyobjc-core>=3.0a1',
        'pyobjc-framework-Cocoa>=3.0a1',
    ],
)
