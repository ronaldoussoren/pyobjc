'''
Wrappers for the "CoreBluetooth" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup

setup(
    name='pyobjc-framework-CoreBluetooth',
    version="3.1",
    description = "Wrappers for the framework CoreBluetooth on Mac OS X",
    long_description=__doc__,
    packages = [ "CoreBluetooth" ],
    setup_requires = [
        'pyobjc-core>=3.1',
    ],
    install_requires = [
        'pyobjc-core>=3.1',
        'pyobjc-framework-Cocoa>=3.1',
    ],
    min_os_level="10.9",
)
