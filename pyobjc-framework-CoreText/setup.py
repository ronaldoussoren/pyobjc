''' 
Wrappers for the "CoreText" framework on MacOSX 10.5 or later. Core Text is an 
advanced, low-level technology for laying out text and handling fonts. It is 
designed for high performance and ease of use.

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

import os
if os.uname()[2] > '9.':
    CFLAGS=["-isysroot", "/"]
else:
    CFLAGS=[]

setup(
    name='pyobjc-framework-CoreText',
    version='2.2b3',
    description = "Wrappers for the framework CoreText on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "CoreText" ],
    package_dir = { '': 'Lib' },
    ext_modules = [
            Extension('CoreText._manual',
                [ 'Modules/_manual.m' ],
                extra_link_args=['-framework', 'CoreServices'],
                extra_compile_args=CFLAGS),
    ],
    install_requires = [ 
        'pyobjc-core>=2.2b3',
        'pyobjc-framework-Cocoa>=2.2b3',
        'pyobjc-framework-Quartz>=2.2b3',
    ],
    package_data = { 
        '': ['*.bridgesupport'] 
    },
    test_suite='PyObjCTest',
    cmdclass = extra_cmdclass,
    options = extra_options('CoreText'),
    zip_safe = True,
)
