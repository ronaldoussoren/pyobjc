'''
Wrappers for the "ApplicationServices" framework on MacOSX 10.5 or later. Core Text is an
advanced, low-level technology for laying out text and handling fonts. It is
designed for high performance and ease of use.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

setup(
    name='pyobjc-framework-ApplicationServices',
    version="3.1b1",
    description = "Wrappers for the framework ApplicationServices on Mac OS X",
    long_description=__doc__,
    packages = [ "ApplicationServices", "HIServices" ],
    setup_requires = [
        'pyobjc-core>=3.1b1',
    ],
    install_requires = [
        'pyobjc-core>=3.1b1',
        'pyobjc-framework-Cocoa>=3.1b1',
        'pyobjc-framework-Quartz>=3.1b1',
    ],
)
