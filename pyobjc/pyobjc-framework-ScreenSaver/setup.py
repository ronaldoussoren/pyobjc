''' 
Wrappers for the "ScreenSaver" framework on MacOSX. This frameworks allows
you to write custom screensaver modules.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension

setup(
    name='pyobjc-framework-ScreenSaver',
    version='2.2b4',
    description = "Wrappers for the framework ScreenSaver on Mac OS X",
    packages = [ "ScreenSaver" ],
    install_requires = [ 
        'pyobjc-core>=2.2b4',
        'pyobjc-framework-Cocoa>=2.2b4',
    ],
    ext_modules = [
        Extension('ScreenSaver._inlines',
            [ 'Modules/_ScreenSaver_inlines.m' ],
            extra_link_args=['-framework', 'ScreenSaver']),
    ],
)
