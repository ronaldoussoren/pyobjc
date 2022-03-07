"""
Wrappers for framework 'ServerNotification' on macOS 10.6. This framework
contains the class NSServerNotificationCenter which provides distributed
notifications over the Extensible Messaging and Presence Protocol (XMPP).

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
from pyobjc_setup import setup

VERSION = "8.4"

setup(
    name="pyobjc-framework-ServerNotification",
    description="Wrappers for the framework ServerNotification on macOS",
    min_os_level="10.6",
    max_os_level="10.8",
    packages=["ServerNotification"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
