'''
Wrappers for the "QTKit" framework on macOS.  QTKit is an modern,
object-oriented framework for working with QuickTime media in Cocoa
applications, and is a replacement for the older Carbon-based Quicktime
framework.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

Note that this framework is deprecated in OSX 10.9
'''
from pyobjc_setup import setup, Extension
import os

VERSION="5.1"

setup(
    name='pyobjc-framework-QTKit',
    description = "Wrappers for the framework QTKit on macOS",
    packages = [ "QTKit" ],
    ext_modules = [
        Extension("QTKit._QTKit",
            [ "Modules/_QTKit.m" ],
            extra_link_args=["-framework", "QTKit"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_QTKit')
            ]
        ),
    ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
        'pyobjc-framework-Quartz>='+VERSION,
    ],
    long_description=__doc__,
)
