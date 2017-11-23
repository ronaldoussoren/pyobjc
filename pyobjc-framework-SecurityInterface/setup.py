'''
Wrappers for the "SecurityInterface" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup
import os

VERSION="4.1b1"

setup(
    name='pyobjc-framework-SecurityInterface',
    description = "Wrappers for the framework SecurityInterface on macOS",
    packages = [ "SecurityInterface" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
        #'pyobjc-framework-Security>='+VERSION,
    ],
    long_description=__doc__,
)
