'''
Wrappers for the "ContactsUI" framework on MacOS X 10.11.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

setup(
    name='pyobjc-framework-ContactsUI',
    min_os_level='10.11',
    version="3.1b1",
    description = "Wrappers for the framework ContactsUI on Mac OS X",
    long_description=__doc__,
    packages = [ "ContactsUI" ],
    setup_requires = [
        'pyobjc-core>=3.1b1',
    ],
    install_requires = [
        'pyobjc-core>=3.1b1',
        'pyobjc-framework-Cocoa>=3.1b1',
        'pyobjc-framework-Contacts>=3.1b1',
    ],
    ext_modules = [
        Extension("ContactsUI._ContactsUI",
            [ "Modules/_ContactsUI.m" ],
            extra_link_args=["-framework", "ContactsUI"],
            depends=[
                os.path.join('Modules', fn)
                    for fn in os.listdir('Modules')
                    if fn.startswith('_ContactsUI')
            ]
        ),
    ],
)
