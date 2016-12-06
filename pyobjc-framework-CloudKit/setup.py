'''
Wrappers for the "CloudKit" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup

VERSION="3.2a1"

setup(
    name='pyobjc-framework-CloudKit',
    version="3.2",
    description = "Wrappers for the framework CloudKit on Mac OS X",
    long_description=__doc__,
    packages = [ "CloudKit" ],
    setup_requires = [
        'pyobjc-core>=3.2',
    ],
    install_requires = [
        'pyobjc-core>=3.2',
        'pyobjc-framework-Cocoa>=3.2',
        'pyobjc-framework-CoreLocation>=3.2',
        'pyobjc-framework-CoreData>=3.2',
        'pyobjc-framework-Accounts>=3.2',
    ],
    min_os_level="10.10",
)
