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

VERSION="3.3a0"

setup(
    name='pyobjc-framework-NetFS',
    description = "Wrappers for the framework NetFS on Mac OS X",
    min_os_level='10.6',
    packages = [ "NetFS" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
