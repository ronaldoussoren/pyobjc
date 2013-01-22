'''
Wrappers for the "AddressBook" framework on MacOS X. The Address Book is
a centralized database for contact and other information for people. Appliations
that make use of the AddressBook framework all use the same database.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

setup(
    name='pyobjc-framework-AddressBook',
    version="2.5.1",
    description = "Wrappers for the framework AddressBook on Mac OS X",
    packages = [ "AddressBook" ],
    setup_requires = [
        'pyobjc-core>=2.5.1',
    ],
    install_requires = [
        'pyobjc-core>=2.5.1',
        'pyobjc-framework-Cocoa>=2.5.1',
    ],
    ext_modules = [
        Extension("AddressBook._AddressBook",
            [ "Modules/_AddressBook.m" ],
            extra_link_args=["-framework", "AddressBook"],
            depends=[
                os.path.join('Modules', fn)
                    for fn in os.listdir('Modules')
                    if fn.startswith('_AddressBook') 
            ]
        ),
    ]
)
