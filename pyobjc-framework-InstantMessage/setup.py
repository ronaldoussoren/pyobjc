"""
Wrappers for "InstantMessage" framework on macOS 10.5 or later. This framework
allows you to access iChat information, as well as a way to provide an
auxiliary video source to iChat Theater.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

Note that this framework is deprecated in OSX 10.9, use the Social framework
instead if you target that OSX release.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "12.1"

setup(
    name="pyobjc-framework-InstantMessage",
    description="Wrappers for the framework InstantMessage on macOS",
    min_os_level="10.5",
    packages=["InstantMessage"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Quartz>=" + VERSION,
    ],
    long_description=__doc__,
)
