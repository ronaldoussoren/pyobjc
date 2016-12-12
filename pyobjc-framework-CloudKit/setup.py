'''
Wrappers for the "CloudKit" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup

VERSION="3.3a0"

setup(
    name='pyobjc-framework-CloudKit',
    description = "Wrappers for the framework CloudKit on Mac OS X",
    min_os_level="10.10",
    packages = [ "CloudKit" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
        'pyobjc-framework-CoreLocation>='+VERSION,
        'pyobjc-framework-CoreData>='+VERSION,
        'pyobjc-framework-Accounts>='+VERSION,
    ],
    long_description=__doc__,
)
