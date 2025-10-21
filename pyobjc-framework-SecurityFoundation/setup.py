"""
Wrappers for the "SecurityFoundation" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "12.1"

setup(
    name="pyobjc-framework-SecurityFoundation",
    description="Wrappers for the framework SecurityFoundation on macOS",
    packages=["SecurityFoundation"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Security>=" + VERSION,
    ],
    long_description=__doc__,
)
