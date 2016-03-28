'''
Wrappers for the "Social" framework on MacOS X 10.8 or later.

Note that this framework is only available for 64-bit code.
'''

from pyobjc_setup import setup

VERSION="3.2a1"

setup(
    name='pyobjc-framework-Social',
    version=VERSION,
    description = "Wrappers for the framework Social on Mac OS X",
    long_description=__doc__,
    packages = [ "Social" ],
    setup_requires = [
        'pyobjc-core>=' + VERSION,
    ],
    install_requires = [
        'pyobjc-core>=' + VERSION,
        'pyobjc-framework-Cocoa>=' + VERSION,
    ],
    min_os_level="10.8",
)
