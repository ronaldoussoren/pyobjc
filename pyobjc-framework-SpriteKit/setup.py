"""
Wrappers for the "SpriteKit" framework on macOS introduced in macOS 10.9.

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
    name="pyobjc-framework-SpriteKit",
    description="Wrappers for the framework SpriteKit on macOS",
    min_os_level="10.9",
    packages=["SpriteKit"],
    ext_modules=[
        Extension(
            "SpriteKit._SpriteKit",
            ["Modules/_SpriteKit.m"],
            extra_link_args=["-framework", "SpriteKit"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_SpriteKit")
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
