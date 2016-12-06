'''
Wrappers for the "PreferencePanes" framework on MacOSX. This framework allows
you to write Preference Panes for the "System Preferences" application.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import *

VERSION="3.2a1"

setup(
    name='pyobjc-framework-PreferencePanes',
    version="3.2.1b1",
    description = "Wrappers for the framework PreferencePanes on Mac OS X",
    long_description=__doc__,
    packages = [ "PreferencePanes" ],
    setup_requires = [
        'pyobjc-core>=3.2.1b1',
    ],
    install_requires = [
        'pyobjc-core>=3.2.1b1',
        'pyobjc-framework-Cocoa>=3.2.1b1',
    ],
)
