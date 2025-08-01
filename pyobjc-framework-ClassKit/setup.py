"""
Wrappers for the "ClassKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup, Extension  # noqa: E402

VERSION = "11.1.1"

setup(
    name="pyobjc-framework-ClassKit",
    description="Wrappers for the framework ClassKit on macOS",
    min_os_level="11.0",
    packages=["ClassKit"],
    ext_modules=[
        Extension(
            "ClassKit._ClassKit",
            ["Modules/_ClassKit.m"],
            extra_link_args=["-framework", "ClassKit"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_ClassKit")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
