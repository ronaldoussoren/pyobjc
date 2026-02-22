"""
Wrappers for the "HomeKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup, Extension  # noqa: E402

VERSION = "12.2"

setup(
    name="pyobjc-framework-HomeKit",
    description="Wrappers for the framework HomeKit on macOS",
    min_os_level="26.4",
    packages=["HomeKit"],
    ext_modules=[
        Extension(
            "HomeKit._HomeKit",
            ["Modules/_HomeKit.m"],
            extra_link_args=["-framework", "HomeKit"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_HomeKit")
            ],
        )
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
    ],
    long_description=__doc__,
)
