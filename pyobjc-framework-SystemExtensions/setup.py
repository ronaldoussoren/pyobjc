"""
Wrappers for the "SystemExtensions" framework on macOS.

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
    name="pyobjc-framework-SystemExtensions",
    description="Wrappers for the framework SystemExtensions on macOS",
    min_os_level="10.15",
    packages=["SystemExtensions"],
    ext_modules=[
        Extension(
            "SystemExtensions._SystemExtensions",
            ["Modules/_SystemExtensions.m"],
            extra_link_args=["-framework", "SystemExtensions"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_SystemExtensions")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
