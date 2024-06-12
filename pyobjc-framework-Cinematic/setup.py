"""
Wrappers for the "Cinematic" framework on macOS.

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
    name="pyobjc-framework-Cinematic",
    description="Wrappers for the framework Cinematic on macOS",
    min_os_level="14.0",
    packages=["Cinematic"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-AVFoundation>=" + VERSION,
        "pyobjc-framework-CoreMedia>=" + VERSION,
        "pyobjc-framework-Metal>=" + VERSION,
    ],
    long_description=__doc__,
)
