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
    max_os_level='10.7',
    name='pyobjc-framework-XgridFoundation',
    version="2.4.1b1",
    description = "Wrappers for the framework XgridFoundation on Mac OS X",
    packages = [ "XgridFoundation" ],
    setup_requires = [
        'pyobjc-core>=2.4.1b1',
    ],
    install_requires = [ 
        'pyobjc-core>=2.4.1b1',
        'pyobjc-framework-Cocoa>=2.4.1b1',
    ],
)
