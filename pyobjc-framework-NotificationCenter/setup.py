'''
Wrappers for the "NotificationCenter" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

setup(
    name='pyobjc-framework-NotificationCenter',
    version="3.1b1",
    description = "Wrappers for the framework NotificationCenter on Mac OS X",
    long_description=__doc__,
    packages = [ "NotificationCenter" ],
    ext_modules = [
        Extension("NotificationCenter._NotificationCenter",
            [ "Modules/_NotificationCenter.m" ],
            extra_link_args=["-framework", "NotificationCenter"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_NotificationCenter')
            ]
        ),
    ],
    setup_requires = [
        'pyobjc-core>=3.1b1',
    ],
    install_requires = [
        'pyobjc-core>=3.1b1',
        'pyobjc-framework-Cocoa>=3.1b1',
    ],
    min_os_level="10.10",
)
