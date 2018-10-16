'''
Wrappers for framework 'ServiceManagement' on macOS 10.6. This framework
provides an interface to the system services subsystem, which basicly means
a this provides a secure and object-oriented interface from launchd.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

VERSION="5.1"

setup(
    name='pyobjc-framework-ServiceManagement',
    description = "Wrappers for the framework ServiceManagement on macOS",
    min_os_level='10.6',
    packages = [ "ServiceManagement" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
