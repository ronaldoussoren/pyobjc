''' 
Wrappers for framework 'AppleScriptKit'. 

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

setup(
    name='pyobjc-framework-AppleScriptKit',
    version='2.2b4',
    description = "Wrappers for the framework AppleScriptKit on Mac OS X",
    packages = [ "AppleScriptKit" ],
    install_requires = [ 
        'pyobjc-core>=2.2b4',
        'pyobjc-framework-Cocoa>=2.2b4',
    ],
)
