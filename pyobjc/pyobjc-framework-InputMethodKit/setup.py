''' 
Wrappers for the "InputMethodKit" framework on MacOSX 10.5 or later. The
interfaces in this framework allow you to develop input methods.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

setup(
    min_os_level='10.5',
    name='pyobjc-framework-InputMethodKit',
    version='2.2b4',
    description = "Wrappers for the framework InputMethodKit on Mac OS X",
    packages = [ "InputMethodKit" ],
    install_requires = [ 
        'pyobjc-core>=2.2b4',
        'pyobjc-framework-Cocoa>=2.2b4' 
    ],
)
