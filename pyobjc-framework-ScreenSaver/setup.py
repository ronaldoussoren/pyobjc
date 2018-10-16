'''
Wrappers for the "ScreenSaver" framework on macOS. This frameworks allows
you to write custom screensaver modules.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension

VERSION="5.1"

setup(
    name='pyobjc-framework-ScreenSaver',
    description = "Wrappers for the framework ScreenSaver on macOS",
    packages = [ "ScreenSaver" ],
    ext_modules = [
        Extension('ScreenSaver._inlines',
            [ 'Modules/_ScreenSaver_inlines.m' ],
            extra_link_args=['-framework', 'ScreenSaver']),
    ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
