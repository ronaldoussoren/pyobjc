"""
Wrappers for the "GameKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = "12.1"

setup(
    name="pyobjc-framework-GameKit",
    description="Wrappers for the framework GameKit on macOS",
    min_os_level="10.8",
    packages=["GameKit"],
    ext_modules=[
        Extension(
            "GameKit._GameKit",
            ["Modules/_GameKit.m"],
            extra_link_args=["-framework", "GameKit"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_GameKit")
            ],
        )
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Quartz>=" + VERSION,
    ],
    long_description=__doc__,
)
