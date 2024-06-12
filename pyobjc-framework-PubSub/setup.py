"""
Wrappers for the "PubSub" framework on macOS 10.5 or later.  This framework
offers developers a way to subscribe to web feeds (RSS, Atom) from their
applications.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

Note that this framework is deprecated in OSX 10.9
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "10.3.2"

setup(
    name="pyobjc-framework-PubSub",
    description="Wrappers for the framework PubSub on macOS",
    min_os_level="10.5",
    max_os_level="10.14",
    packages=["PubSub"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
