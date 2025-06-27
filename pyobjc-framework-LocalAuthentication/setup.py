"""
Wrappers for the "LocalAuthentication" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = "11.1.1"

setup(
    name="pyobjc-framework-LocalAuthentication",
    description="Wrappers for the framework LocalAuthentication on macOS",
    min_os_level="10.10",
    packages=["LocalAuthentication"],
    ext_modules=[
        Extension(
            "LocalAuthentication._LocalAuthentication",
            ["Modules/_LocalAuthentication.m"],
            extra_link_args=["-framework", "LocalAuthentication"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_LocalAuthentication")
            ],
        )
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Security>=" + VERSION,
    ],
    long_description=__doc__,
)
