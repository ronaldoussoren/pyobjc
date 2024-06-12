"""
Wrappers for framework 'ServiceManagement' on macOS 10.6. This framework
provides an interface to the system services subsystem, which basically means
a this provides a secure and object-oriented interface from launchd.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "10.3.2"

setup(
    name="pyobjc-framework-ServiceManagement",
    description="Wrappers for the framework ServiceManagement on macOS",
    min_os_level="10.6",
    packages=["ServiceManagement"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
