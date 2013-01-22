'''
Wrappers for the "Message" framework on MacOSX. This framework contains a
number of utilities for sending e-mail.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup
setup(
    name='pyobjc-framework-Message',
    version="2.5.1",
    description = "Wrappers for the framework Message on Mac OS X",
    packages = [ "Message" ],
    setup_requires = [
        'pyobjc-core>=2.5.1',
    ],
    install_requires = [
        'pyobjc-core>=2.5.1',
        'pyobjc-framework-Cocoa>=2.5.1',
    ],
)
