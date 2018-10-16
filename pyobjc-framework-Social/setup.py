'''
Wrappers for the "Social" framework on macOS 10.8 or later.

Note that this framework is only available for 64-bit code.
'''

from pyobjc_setup import setup

VERSION="5.1"

setup(
    name='pyobjc-framework-Social',
    description = "Wrappers for the framework Social on macOS",
    min_os_level="10.8",
    packages = [ "Social" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
