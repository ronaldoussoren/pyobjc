"""
Wrappers for the "GameplayKit" framework on macOS.

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
    name="pyobjc-framework-GameplayKit",
    description="Wrappers for the framework GameplayKit on macOS",
    min_os_level="10.11",
    packages=["GameplayKit"],
    ext_modules=[
        Extension(
            "GameplayKit._GameplayKit",
            ["Modules/_GameplayKit.m"],
            extra_link_args=["-framework", "GameplayKit"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_GameplayKit")
            ],
        )
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-SpriteKit>=" + VERSION,
    ],
    long_description=__doc__,
)
