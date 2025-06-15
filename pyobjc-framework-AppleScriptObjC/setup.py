"""
Wrappers for framework 'AppleScriptObjC' on macOS 10.6. This framework is
not useful for most users, it provides additional functionality for AppleScript
based application bundles.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "11.1.1"

setup(
    name="pyobjc-framework-AppleScriptObjC",
    description="Wrappers for the framework AppleScriptObjC on macOS",
    min_os_level="10.6",
    packages=["AppleScriptObjC"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
