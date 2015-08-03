'''
Wrappers for the "NetFS" framework on MacOS X. The Address Book is
a centralized database for contact and other information for people. Appliations
that make use of the NetFS framework all use the same database.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup
import os

setup(
    name='pyobjc-framework-NetFS',
    version="3.1b1",
    description = "Wrappers for the framework NetFS on Mac OS X",
    long_description=__doc__,
    packages = [ "NetFS" ],
    setup_requires = [
        'pyobjc-core>=3.1b1',
    ],
    install_requires = [
        'pyobjc-core>=3.1b1',
        'pyobjc-framework-Cocoa>=3.1b1',
    ],
    min_os_level='10.6',
)
