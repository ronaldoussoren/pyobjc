"""
Wrappers for the "HealthKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = "12.0.1"

setup(
    name="pyobjc-framework-HealthKit",
    description="Wrappers for the framework HealthKit on macOS",
    min_os_level="13.0",
    packages=["HealthKit"],
    ext_modules=[
        Extension(
            "HealthKit._HealthKit",
            ["Modules/_HealthKit.m"],
            extra_link_args=["-framework", "HealthKit"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_HealthKit")
            ],
        ),
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
    ],
    long_description=__doc__,
)
