'''
Wrappers for the "Network" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="5.1"

setup(
    name='pyobjc-framework-Network',
    description = "Wrappers for the framework Network on macOS",
    min_os_level="10.14",
    packages = [ "Network" ],
    ext_modules = [
        Extension("Network._Network",
            [ "Modules/_Network.m" ],
            extra_link_args=["-framework", "Network"],
        ),
    ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
