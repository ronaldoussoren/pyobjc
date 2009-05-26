''' 
Wrappers for the "AddressBook" framework on MacOS X. The Address Book is
a centralized database for contact and other information for people. Appliations
that make use of the AddressBook framework all use the same database.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

try:
    from PyObjCMetaData.commands import extra_cmdclass, extra_options
except ImportError:
    extra_cmdclass = {}
    extra_options = lambda name: {}

setup(
    name='pyobjc-framework-AddressBook',
    version="2.2b3",
    description = "Wrappers for the framework AddressBook on Mac OS X",
    long_description = __doc__,
    author = 'Ronald Oussoren',
    author_email = 'pyobjc-dev@lists.sourceforge.net',
    url= 'http://pyobjc.sourceforge.net/',
    platforms = [ "MacOS X" ],
    packages = [ "AddressBook" ],
    package_dir = { '': 'Lib' },
    install_requires = [ 
        'pyobjc-core>=2.2b3',
        'pyobjc-framework-Cocoa>=2.2b3',
    ],
    package_data = { 
        '': ['*.bridgesupport'] 
    },
    cmdclass = extra_cmdclass,
    options = extra_options('AddressBook'),
    zip_safe = True,
    test_suite='PyObjCTest',
)
