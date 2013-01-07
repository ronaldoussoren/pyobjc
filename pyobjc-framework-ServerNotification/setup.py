'''
Wrappers for framework 'ServerNotification' on MacOSX 10.6. This framework
contains the class NSServerNotificationCenter which provides distributed
notifications over the Extensible Messaging and Presence Protocol (XMPP).

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

setup(
    min_os_level='10.6',
    name='pyobjc-framework-ServerNotification',
    version="2.5.1b1",
    description = "Wrappers for the framework ServerNotification on Mac OS X",
    packages = [ "ServerNotification" ],
    setup_requires = [
        'pyobjc-core>=2.5.1b1',
    ],
    install_requires = [
        'pyobjc-core>=2.5.1b1',
        'pyobjc-framework-Cocoa>=2.5.1b1',
    ],
)
