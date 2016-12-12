'''
Wrappers for the "Social" framework on MacOS X 10.8 or later.

Note that this framework is only available for 64-bit code.
'''

from pyobjc_setup import setup

VERSION="3.3a0"

setup(
    name='pyobjc-framework-Social',
    description = "Wrappers for the framework Social on Mac OS X",
    min_os_level="10.8",
    packages = [ "Social" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
