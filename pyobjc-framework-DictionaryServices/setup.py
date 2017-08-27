'''
Wrappers for the "DictionaryServices" framework on macOS 10.5 or later.

Dictionary Services lets you create your own custom dictionaries that users
can access through the Dictionary application. You also use these services to
access dictionaries programatically and to support user access to dictionary
look-up through a contextual menu.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension
import os

VERSION="4.0b1"

setup(
    name='pyobjc-framework-DictionaryServices',
    description = "Wrappers for the framework DictionaryServices on macOS",
    min_os_level='10.5',
    packages = [ "DictionaryServices" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
