''' 
PyObjC wrappers for the framework "CFNetwork", part of "CoreServices" on 
MacOSX.

The CFNetwork framework provides a library of abstractions for networking
protocols. The most interesting bits for Python programmers are the
API's for working with proxy autoconfiguration and the API's for networking
diagnotics.

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
if os.uname()[2] >= '9.':
    CFLAGS=["-isysroot", "/"]
else:
    CFLAGS=[]

setup(
    name='pyobjc-framework-CFNetwork',
    version='2.2b3',
    description = "Wrappers for the framework CFNetwork on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "CFNetwork" ],
    package_dir = { '': 'Lib/' },
    install_requires = [ 
        'pyobjc-core>=2.2b3',
        'pyobjc-framework-Cocoa>=2.2b3',
    ],
    package_data = { 
        '': ['*.bridgesupport'] 
    },
    ext_modules = [
        Extension("CFNetwork._manual",
            ["Modules/_manual.m"],
            extra_link_args=['-framework', 'CoreServices'],
            extra_compile_args=CFLAGS,
        ),
    ],
    test_suite='PyObjCTest',
    cmdclass = extra_cmdclass,
    options = extra_options('CFNetwork'),
    zip_safe = True,
)
