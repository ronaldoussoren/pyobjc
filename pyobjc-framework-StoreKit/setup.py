"""
Wrappers for the "StoreKit" framework on macOS 10.7 or later.

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
    name="pyobjc-framework-StoreKit",
    description="Wrappers for the framework StoreKit on macOS",
    min_os_level="10.7",
    packages=["StoreKit"],
    ext_modules=[
        Extension(
            "StoreKit._StoreKit",
            ["Modules/_StoreKit.m"],
            extra_link_args=["-framework", "StoreKit"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_StoreKit")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
