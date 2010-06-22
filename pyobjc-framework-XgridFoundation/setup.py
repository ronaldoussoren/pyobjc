''' 
Wrappers for the "XgridFoundation" framework on MacOSX. This framework 
supports the development of applications that monitor or control jobs 
processed by Xgrid clusters.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

setup(
    name='pyobjc-framework-XgridFoundation',
    version="2.3b1",
    description = "Wrappers for the framework XgridFoundation on Mac OS X",
    packages = [ "XgridFoundation" ],
    install_requires = [ 
        'pyobjc-core>=2.3b1',
        'pyobjc-framework-Cocoa>=2.3b1',
    ],
)
