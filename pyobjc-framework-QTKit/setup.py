'''
Wrappers for the "QTKit" framework on MacOSX.  QTKit is an modern,
object-oriented framework for working with QuickTime media in Cocoa
applications, and is a replacement for the older Carbon-based Quicktime
framework.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

setup(
    name='pyobjc-framework-QTKit',
    version="2.5.1",
    description = "Wrappers for the framework QTKit on Mac OS X",
    packages = [ "QTKit" ],
    setup_requires = [
        'pyobjc-core>=2.5.1',
    ],
    install_requires = [
        'pyobjc-core>=2.5.1',
        'pyobjc-framework-Cocoa>=2.5.1',
        'pyobjc-framework-Quartz>=2.5.1',
    ],
)
