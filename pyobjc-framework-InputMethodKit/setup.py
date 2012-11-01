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
    version="2.4",
    description = "Wrappers for the framework InputMethodKit on Mac OS X",
    packages = [ "InputMethodKit" ],
    setup_requires = [
        'pyobjc-core>=2.4',
    ],
    install_requires = [ 
        'pyobjc-core>=2.4',
        'pyobjc-framework-Cocoa>=2.4',
    ],
)
