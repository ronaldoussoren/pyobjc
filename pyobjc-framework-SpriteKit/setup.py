'''
Wrappers for the "SpriteKit" framework on MacOS X introduced in Mac OS X 10.9.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

setup(
    name='pyobjc-framework-SpriteKit',
    version="3.1",
    description = "Wrappers for the framework SpriteKit on Mac OS X",
    packages = [ "SpriteKit" ],
    setup_requires = [
        'pyobjc-core>=3.1',
    ],
    install_requires = [
        'pyobjc-core>=3.1',
        'pyobjc-framework-Cocoa>=3.1',
        'pyobjc-framework-Quartz>=3.1',
    ],
)
