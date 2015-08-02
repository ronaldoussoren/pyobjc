'''
Wrappers for the "GameCenter" framework on MacOS X. The Address Book is
a centralized database for contact and other information for people. Appliations
that make use of the GameCenter framework all use the same database.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

setup(
    name='pyobjc-framework-GameCenter',
    version="3.1b1",
    description = "Wrappers for the framework GameCenter on Mac OS X",
    long_description=__doc__,
    packages = [ "GameCenter" ],
    setup_requires = [
        'pyobjc-core>=3.1b1',
    ],
    install_requires = [
        'pyobjc-core>=3.1b1',
        'pyobjc-framework-Cocoa>=3.1b1',
    ],
    ext_modules = [
        Extension("GameCenter._GameCenter",
            [ "Modules/_GameCenter.m" ],
            extra_link_args=["-framework", "GameKit"],
            depends=[
                os.path.join('Modules', fn)
                    for fn in os.listdir('Modules')
                    if fn.startswith('_GameCenter')
            ]
        ),
    ],
    min_os_level='10.8',
)
