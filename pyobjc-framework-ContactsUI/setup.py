'''
Wrappers for the "ContactsUI" framework on macOS 10.11.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="5.1"

setup(
    name='pyobjc-framework-ContactsUI',
    description = "Wrappers for the framework ContactsUI on macOS",
    min_os_level='10.11',
    packages = [ "ContactsUI" ],
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
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
        'pyobjc-framework-Contacts>='+VERSION,
    ],
    long_description=__doc__,
)
