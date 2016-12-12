'''
Wrappers for the "SafariServices" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="3.2a1"

setup(
    name='pyobjc-framework-SafariServices',
    version="3.2.1",
    description = "Wrappers for the framework SafariServices on Mac OS X",
    long_description=__doc__,
    packages = [ "SafariServices" ],
    setup_requires = [
        'pyobjc-core>=3.2.1',
    ],
    install_requires = [
        'pyobjc-core>=3.2.1',
        'pyobjc-framework-Cocoa>=3.2.1',
    ],
    min_os_level="10.11",
    ext_modules = [
        Extension("SafariServices._SafariServices",
            [ "Modules/_SafariServices.m" ],
            extra_link_args=["-framework", "SafariServices"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_SafariServices')
            ]
        ),
    ],
)
