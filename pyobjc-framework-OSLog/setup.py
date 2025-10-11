"""
Wrappers for the "OSLog" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = "12.0"

setup(
    name="pyobjc-framework-OSLog",
    description="Wrappers for the framework OSLog on macOS",
    min_os_level="10.15",
    packages=["OSLog"],
    ext_modules=[
        Extension(
            "OSLog._OSLog",
            ["Modules/_OSLog.m"],
            extra_link_args=["-framework", "OSLog"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_OSLog")
            ],
        )
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-CoreMedia>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Quartz>=" + VERSION,
    ],
    long_description=__doc__,
)
