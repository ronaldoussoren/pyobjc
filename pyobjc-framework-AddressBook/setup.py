''' 
Wrappers for framework 'AddressBook'. 

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, Extension

try:
    from PyObjCMetaData.commands import extra_cmdclass, extra_options
except ImportError:
    extra_cmdclass = {}
    extra_options = lambda name: {}

setup(
    name='pyobjc-framework-AddressBook',
    version="2.0",
    description = "Wrappers for the framework AddressBook on Mac OS X",
    long_description = __doc__,
    author = 'Ronald Oussoren',
    author_email = 'pyobjc-dev@lists.sourceforge.net',
    url= 'http://pyobjc.sourceforge.net/',
    platforms = [ "MacOS X" ],
    packages = [ "AddressBook" ],
    package_dir = { '': 'Lib' },
    ext_modules = [
        Extension('AddressBook._callback',
                [ 'Modules/_callback.m' ],
                extra_link_args=['-framework', 'AddressBook']),
    ],
    setup_requires = [ 
    ],
    install_requires = [ 
        'pyobjc-core>=2.0',
        'pyobjc-framework-Cocoa>=2.0',
    ],
    dependency_links = [],
    package_data = { 
        '': ['*.bridgesupport'] 
    },
    cmdclass = extra_cmdclass,
    options = extra_options('AddressBook'),
    zip_safe = True,
    test_suite='PyObjCTest',
)
