'''
Wrappers for the "OSAKit" framework on macOS. The Address Book is
a centralized database for contact and other information for people. Appliations
that make use of the OSAKit framework all use the same database.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup
import os

VERSION="5.0a1"

setup(
    name='pyobjc-framework-OSAKit',
    description = "Wrappers for the framework OSAKit on macOS",
    packages = [ "OSAKit" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
