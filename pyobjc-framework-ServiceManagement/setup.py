'''
Wrappers for framework 'ServiceManagement' on MacOSX 10.6. This framework
provides an interface to the system services subsystem, which basicly means
a this provides a secure and object-oriented interface from launchd.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

setup(
    min_os_level='10.6',
    name='pyobjc-framework-ServiceManagement',
    version="2.5.1",
    description = "Wrappers for the framework ServiceManagement on Mac OS X",
    packages = [ "ServiceManagement" ],
    setup_requires = [
        'pyobjc-core>=2.5.1',
    ],
    install_requires = [
        'pyobjc-core>=2.5.1',
        'pyobjc-framework-Cocoa>=2.5.1',
    ],
)
